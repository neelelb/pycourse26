# test_data_loading.py

from pycourse26.data import fetch_data

# TODO: use pytest fixture to laod the different formats
# @pytest.fixture
# def format_contents():
#     ...


def test_load_data(tmp_path):
    format1 = """\
onset   duration    trial_type  rewards
13  0   options_partner  n/a
16  0   decision_risky_partner    25
20.072093   0   outcome_other_neg_partner      0
27.661415   0   options_solo       0
"""
    format2 = """\
onset,duration,trial_type,rewards
13.0,0,options_partner,
16.0,0,decision_risky_partner,25.0
20.072093,0,outcome_other_neg_partner,0.0
27.661415,0,options_solo,0.0
"""
    format3 = """\
onset,duration,trial_type,rewards
13.0,0,options_partner,
16.0,0,decision_risky_partner,25.0
"""
    format4 = """\
onset,,duration,trial_type,rewards
13.0,0,options_partner,
16.0,0,decision_risky_partner,25.0
27.661415,0,options_solo,0.0
33.796415,0,decision_safe_solo,0.0
"""

    for i, format_content in enumerate((format1, format2, format3, format4)):
        path = tmp_path / f"format-{i}.csv"
        path.write_text(format_content)
        data = fetch_data(path)
        assert list(data.columns) == ["onset", "duration", "trial_type", "rewards"]