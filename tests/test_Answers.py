def test_record_reader():
    from Answers import record_reader
    input_folder = "../test_folder/Data"
    records = record_reader(input_folder)
    assert records['record_files'][0] == ['200.hea']
    assert records['record_files'][9] == ['212.hea']
    assert records['record_files'][-1] == ['214.hea']
    assert records['record_objs'][0].record_name == ['200']
    assert records['record_objs'][9].record_name == ['212']
    assert records['record_objs'][7].p_signal.shape == (2,650000)


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