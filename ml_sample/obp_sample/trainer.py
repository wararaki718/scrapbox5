from sklearn.linear_model import LogisticRegression
from obp.policy import IPWLearner
from obp.types import BanditFeedback


class Trainer:
    def __init__(self):
        pass

    def train(self, X: BanditFeedback, n_actions: int) -> IPWLearner:
        ipw_learner = IPWLearner(
            n_actions=n_actions,
            base_classifier=LogisticRegression(C=100, random_state=12345)
        )

        ipw_learner.fit(
            context=X["context"],
            action=X["action"],
            reward=X["reward"],
            pscore=X["pscore"]
        )

        return ipw_learner
