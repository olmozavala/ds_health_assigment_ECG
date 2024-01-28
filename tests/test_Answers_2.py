from answers_module import heart_beats_summary
import os
import pytest
from os.path import join
import wfdb

def record_fix(file_name):
    hea_path = "./test_folder/Data"
    if not(os.path.exists(hea_path)):
        hea_path = "../test_folder/Data"

    record = wfdb.rdrecord(join(hea_path, file_name))
    annot = wfdb.rdann(join(hea_path, file_name), sampfrom=0, extension='atr')
    return record, annot

def test_heart_beats_summary():
    record, annot = record_fix('200')
    summary = heart_beats_summary(annot)

    assert isinstance(summary, dict)
    assert 'heart_beats' in summary
    assert 'mean_heart_rate' in summary
    assert 'perc_normal_beats' in summary

    assert summary['heart_beats'] == pytest.approx(2644, abs=3)
    assert summary['mean_heart_rate'] == pytest.approx(87, abs=3)
    assert summary['perc_normal_beats'] == pytest.approx(65, abs=3.1)
    
    # % ----------------------------------
    record, annot = record_fix('202')
    summary = heart_beats_summary(annot)
    assert isinstance(summary, dict)
    assert 'heart_beats' in summary
    assert 'mean_heart_rate' in summary
    assert 'perc_normal_beats' in summary

    # Test approximate values
    assert summary['heart_beats'] == pytest.approx(2138, abs=3)
    assert summary['mean_heart_rate'] == pytest.approx(71, abs=3)
    assert summary['perc_normal_beats'] == pytest.approx(96, abs=3.1)
