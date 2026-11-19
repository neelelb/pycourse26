from pycourse26.preprocessing import cast_rewards_col, pipeline
import pandas as pd
import numpy as np
from pandas.testing import assert_frame_equal


def test_cast_rewards_col_step():
    inp = pd.DataFrame({"rewards": [1, 2, "-2O.O"]})
    out = cast_rewards_col(inp)
    exp = pd.DataFrame({"rewards": [1, 2, np.nan]})
    assert_frame_equal(out, exp)


def test_pipeline(tmp_path):
    input_content = """\
onset   duration    trial_type  rewards
13  0   options_partner  n/a
16  0   decision_risky_partner    25
16  0   decision_risky_partner    O.O
20.072093   0   outcome_other_neg_partner      0
27.661415   0   options_solo       0
33.796415   0   decision_safe_solo     0
n/a   0   decision_safe_solo     0
    """
    data_path = tmp_path / "input.csv"
    data_path.write_text(input_content)

    output_path = tmp_path / "output.csv"
    onset_value = 2

    out = pipeline(data_path, output_path=output_path, onset_value=onset_value)
    exp = pd.DataFrame({
        "onset": [16, 16, 33.796415],
        "duration": [0, 0, 0],
        "trial_type": [
            "decision_risky_partner",
            "decision_risky_partner",
            "decision_safe_solo",
        ],
        "rewards": [0.92582, -1.38873, 0.46291],
    }).reset_index(drop=True)

    out_written = pd.read_csv(output_path)

    assert_frame_equal(out.reset_index(drop=True), exp)
    assert_frame_equal(out_written, exp)