import pytest
from bolted_lap_joint_design import design_lap_joint

# Parameterize over loads from 0 to 100 kN and thicknesses from the given list.
@pytest.mark.parametrize("P", [0, 10, 25, 50, 75, 100])
@pytest.mark.parametrize("t1", [6, 8, 10, 12, 16, 20, 24])
@pytest.mark.parametrize("t2", [6, 8, 10, 12, 16, 20, 24])
def test_minimum_bolt_design(P, t1, t2):
    w = 150  # Fixed plate width in mm
    if P == 0:
        # With zero load, the design function should raise a ValueError.
        with pytest.raises(ValueError, match="No suitable design found"):
            design_lap_joint(P, w, t1, t2)
    else:
        # For any positive load, a design should be found.
        design = design_lap_joint(P, w, t1, t2)
        assert design["number_of_bolts"] >= 2, (
            f"Design for P={P}, t1={t1}, t2={t2} returned less than 2 bolts."
        )
