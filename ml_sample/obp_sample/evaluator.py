from pathlib import Path

from obp.dataset import SyntheticBanditDataset
from obp.ope import (
    OffPolicyEvaluation,
    RegressionModel,
    InverseProbabilityWeighting as IPS,
    DoublyRobust as DR
)
from obp.policy import IPWLearner, Random
from obp.types import BanditFeedback
from sklearn.linear_model import LogisticRegression


class Evaluator:
    def __init__(self, n_actions: int):
        self._random = Random(n_actions=n_actions)
        self._model = RegressionModel(
            n_actions=n_actions,
            base_model=LogisticRegression(C=100, random_state=12345)
        )

    def evaluate(self, learner: IPWLearner, X: BanditFeedback, dataset: SyntheticBanditDataset):
        ipw_actions = learner.predict(context=X["context"])
        random_actions = self._random.compute_batch_action_dist(n_rounds=X["n_rounds"])

        rewards = self._model.fit_predict(
            context=X["context"],
            action=X["action"],
            reward=X["reward"],
            random_state=12345
        )

        ope = OffPolicyEvaluation(
            bandit_feedback=X,
            ope_estimators=[IPS(), DR()]
        )
        ope.visualize_off_policy_estimates_of_multiple_policies(
            policy_name_list=["IPWLearner", "Random"],
            action_dist_list=[
                ipw_actions,
                random_actions
            ],
            estimated_rewards_by_reg_model=rewards,
            random_state=12345,
            fig_dir=Path(".")
        )

        ipw_results = dataset.calc_ground_truth_policy_value(
            expected_reward=X["expected_reward"],
            action_dist=ipw_actions
        )
        random_results = dataset.calc_ground_truth_policy_value(
            expected_reward=X["expected_reward"],
            action_dist=random_actions
        )

        print(f"ipw performance: {ipw_results}")
        print(f"random performance: {random_results}")
