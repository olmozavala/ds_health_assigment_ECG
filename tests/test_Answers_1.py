import pytest
import os
from answers_module import record_reader
import wfdb

def test_record_reader():
    hea_path = "./test_folder/Data"
    records = record_reader(hea_path)

    assert isinstance(records, list)

    for record in records:
        assert isinstance(record, dict)
        assert 'file_name' in record
        assert 'record_obj' in record
        assert 'annot_obj' in record
        assert isinstance(record['file_name'], str)
        assert isinstance(record['record_obj'], wfdb.io.record.Record)
        assert isinstance(record['annot_obj'], wfdb.io.annotation.Annotation)

        if record['file_name'] == '200':
            assert record['record_obj'].record_name == '200'
            assert record['record_obj'].n_sig == 2
            assert record['record_obj'].fs == 360
            assert record['record_obj'].sig_len == 650000
            assert record['record_obj'].p_signal.shape == (650000, 2)
            assert record['record_obj'].sig_name == ['MLII', 'V1']
            assert record['record_obj'].sig_len == 650000
            assert record['record_obj'].n_sig == 2
            assert record['record_obj'].fs == 360
            assert record['record_obj'].counter_freq == None