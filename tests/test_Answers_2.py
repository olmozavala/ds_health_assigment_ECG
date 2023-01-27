def test_heart_beats_summary():
    from Answers import heart_beats_summary, os
    from pyecg import ECGRecord
    import pytest
    input_file = "../test_folder/Data/212.hea"
    record = ECGRecord.from_wfdb(input_file)
    output = heart_beats_summary(record)
    assert output['heart_beats'] == pytest.approx(2762, 2)
    assert output['mean_heart_rate'] == pytest.approx(91, 1)
    assert output['perc_normal_beats'] == pytest.approx(.33, .05)