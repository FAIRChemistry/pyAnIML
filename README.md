<h1 align="center">
  PyAnIML<br>
</h1>
<p align="center"> 
Library that integrates the AnIML data model into an object oriented interface. </br>PyAnIML allows setting up valid AnIML documents and supports export/import to and from JSON</p>

## ⚡️ Quick start
Get started with PyEnzyme by running the following command 

```
# Using PyPI
python -m pip install pyaniml
```

Or build by source
```
git clone https://github.com/FAIRChemistry/pyAnIML.git
cd pyAniML
python3 setup.py install
```

## ⚙️ Example code

```python
import pyaniml as animl

# Initialize AnIML document
animldoc = animl.AnIMLDocument()

# Create and add Sample
sample = animl.Sample(id="S1", name="Sample1")
sample_param = animl.Parameter(name="param1", parameter_type="String", value="Lol")
sample.add_property(sample_param)
animldoc.add_sample(sample)

# Create and add experiment step
exp_step = animl.ExperimentStep(name="Exp_Step", experiment_step_id="ID1")

# Add sample reference
exp_step.add_sample_reference(
    sample=sample, role="Role", sample_purpose="Purpose"
)

# Create method
device = animl.Device(name="Device", firmware_version="1.0", serial_number="123")
exp_step.add_method(device)
# Create result
data = animl.IndividualValueSet(data=[1, 2, 3, 4, 5])
series = animl.Series(name="Series", id="Series1", data=data,
                data_type="Int32", dependency="dependent", plot_scale="none"
                )
exp_step.add_result(series)

# Finally, add exp step to document
animldoc.add_experiment_step(exp_step)
xml_string = animldoc.toXML()
print(animl.AnIMLDocument.fromXMLString(xml_string))
```
<sub>(Code should run as it is)</sup>

## ⚠️ License

`PyAnIML` is free and open-source software licensed under the [MIT License](https://github.com/FAIRChemistry/pyAnIML/blob/main/LICENSE). 
