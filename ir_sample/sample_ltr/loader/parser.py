class LineParser:
    def __init__(self):
        self._column_names = {
            "qid": "qid",
            "1": "tf_of_body",
            "2": "tf_of_anchor",
            "3": "tf_of_title",
            "4": "tf_of_url",
            "5": "tf_of_whole_document",
            "6": "idf_of_body",
            "7": "idf_of_anchor",
            "8": "idf_of_title",
            "9": "idf_of_url",
            "10": "idf_of_whole_document",
            "11": "tfidf_of_body",
            "12": "tfidf_of_anchor",
            "13": "tfidf_of_title",
            "14": "tfidf_of_url",
            "15": "tfidf_of_whole_document",
            "16": "dl_of_body",
            "17": "dl_of_anchor",
            "18": "dl_of_title",
            "19": "dl_of_url",
            "20": "dl_of_whole_document",
            "21": "bm25_of_body",
            "22": "bm25_of_anchor",
            "23": "bm25_of_title",
            "24": "bm25_of_url",
            "25": "bm25_of_whole_document",
            "26": "lmir_abs_of_body",
            "27": "lmir_abs_of_anchor",
            "28": "lmir_abs_of_title",
            "29": "lmir_abs_of_url",
            "30": "lmir_abs_of_whole_document",
            "31": "lmir_dir_of_body",
            "32": "lmir_dir_of_anchor",
            "33": "lmir_dir_of_title",
            "34": "lmir_dir_of_url",
            "35": "lmir_dir_of_whole_document",
            "36": "lmir_jm_of_body",
            "37": "lmir_jm_of_anchor",
            "38": "lmir_jm_of_title",
            "39": "lmir_jm_of_url",
            "40": "lmir_jm_of_whole_document",
            "41": "page_rank",
            "42": "inlink_number",
            "43": "outlink_number",
            "44": "number_of_slash_in_url",
            "45": "length_of_url",
            "46": "number_of_child_page"
        }

    def parse(self, line: str) -> dict:
        items = line.split("#")
        key_values = items[0].strip().split()

        feature = dict()
        for key_value in key_values[1:]:
            key, value = key_value.split(":")
            feature[self._column_names[key]] = float(value)
        feature["qid"] = int(feature["qid"])
        feature["label"] = int(key_values[0])
        feature["label_norm"] = int(feature["label"] > 0)

        params = items[1].strip().replace(" = ", "=").split()
        for param in params:
            key, value = param.split("=")
            if key == "docid":
                feature[key] = value
            else:
                feature[key] = float(value)
        return feature
