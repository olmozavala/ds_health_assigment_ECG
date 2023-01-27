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
