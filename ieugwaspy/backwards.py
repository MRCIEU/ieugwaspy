"""Backwards compatibility for old IDs
"""


def legacy_ids(study_ids):
    """Handle legacy study IDs, returning the new format

    Parameters:
        study_ids: List of study IDs (new or old)

    Returns:
        result: List of new study IDs

    """
    legacy_id_subs = {
        "UKB-a:": "ukb-a-",
        "UKB-b:": "ukb-b-",
        "UKB-c:": "ukb-c-",
        "IEU-a:": "ieu-a-",
        "\\D": "ieu-a-",
    }
    result = []
    for id in study_ids:
        for legacy_id in legacy_id_subs.keys():
            if id.find(legacy_id) >= 0:
                id = id.replace(legacy_id, legacy_id_subs[legacy_id])
        result.append(id)
    return result
