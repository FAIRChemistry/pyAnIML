from pyaniml import AnIMLDocument, Sample, Series, Parameter, ExperimentStep, Device, IndividualValueSet

# Initialize AnIML document
animldoc = AnIMLDocument()

# Create and add Sample
sample = Sample(id="S1", name="Sample1")
sample_param = Parameter(name="param1", parameter_type="String", value="Lol")

sample.add_property(sample_param)
animldoc.add_sample(sample)

# Create and add experiment step
exp_step = ExperimentStep(name="Exp_Step", experiment_step_id="ID1")

# Add sample reference
exp_step.add_sample_reference(
    sample=sample, role="Role", sample_purpose="Purpose"
)

# Create method
device = Device(name="Device", firmware_version="1.0", serial_number="123")
exp_step.add_method(device)

# Create result
data = IndividualValueSet(data=[1, 2, 3, 4, 5])
series = Series(name="Series", id="Series1", data=data,
                data_type="Int32", dependency="dependent", plot_scale="none"
                )
exp_step.add_result(series)

# Finally, add exp step to document
animldoc.add_experiment_step(exp_step)

xml_string = animldoc.toXML()
print(xml_string)
