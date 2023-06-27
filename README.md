# LDMXML
This project was a Machine Learning project for my Master Thesis, the goal of which was to use Artificial Neural Networks (ANNs) to classify events from the Light Dark Matter eXperiment depending on the number of electrons in each event.  

The project uses simulated data generated via the the LDMX software (https://github.com/LDMX-Software/ldmx-sw).  The data is produced in a series of ROOT files and so Uproot is necessary for dealing with the data. The project is built in python 3.10 and is built with Tensorflow and Keras as well as PyTorch Geometric.  The data used in this project was generated as a series of ROOT files with 10000 events in each and the data extraction can be seen in DataExtractor.py.

Four different types of ANNs were trained for this task: A convolutional neural network (CNN), recurrent neural network (RNN), graph neural network (GNN), and a combined CNN and RNN neural network. The CNN, RNN, and combination networks were built using Tensorflow while the GNN were built using PyTorch Geometric. 

The different ANNs are designed to work with data from the Electromagnetic Calorimeter (Ecal) and the Trigger Scintillator. The data from the Equal are located in the EcalRecHits_sim parts of the ROOT file generated with the data while the Trigger Scintillator data is located in TrigScintScoringPlaneHits_sim. The models can be used with the Cartesian coordinate version of the data but is currently designed to use the Model, Layer, and Cell number of each hit in the event. This requires the use of the EcalID for each that can be converted to Module, Layer, and Cell ID using the EcalID() function from libDetDescr. The current preprocessing required for the different models included here can of course be changed and is something I would actively encourage to investigate the possible effects but currently they have the following forms:

CNN:

The CNN models use 3D convolutional layers and therefore require a 3D array as input. If only the Ecal data is used the arrat has the shape (34,7,450) while if the Ecal data is combined with the Trigger Scintillator data the shape is (35,8,450) the increased size comes from accounting for adding the Trigger Scintillator data for each hit. Worth testing is if by increasing the dimension size a deeper network can be created, for example by changing to (35,50,450) more layers could be used which might have some benefit on performance. The model can be seen in the CNNModelANN.py. 

RNN:

Each hit is converted into a value in a time series for each event. The RNN networks requires that the events are equal in length so they need to be padded to ensure they are all the same length. This padding is performed with zeros that are subsequently ignored by the network while performing the training. The largest length for the Ecal events was found to be 450 while for the Ecal and Trigger Scintillator 451 and 453 were used depending on the implementation. An example can be seen in RNNModelANN.py.


GNN: 

Each hit is treated as a node in a graph with features (energy, module, layer, cell) while the edges are calculated using geometric radius which is set to 40 for this data set. There is no real difference between the Ecal and the Ecal and Trigger Scintillator models as the number of hits are just different and there is no need for padding as the number of nodes is not a set number. An example can be seen in GNNModelANN.py. [The model included unfortunately does not work yet however this provides a basis to build of.]

Combined CNN and RNN:

The same array shape is used as for the CNN but the 34 or 35 now refers to the number of frames in the “video” that is being processed. Note that the array is reshaped into (34,7,450,1) and (35,8,450,1) as this becomes the expected shape for this type of network. An example can be seen in CRModelANN.py


Note on Data Generation: 
When generating the data a recommendation would be to save each event as a separate file. This allows for an easier time when using the generators later as changing the batch size becomes much easier to deal with. A generator only loads specific files at a time since trying to load all of the data at once overloads the RAM. 

Note on Training:
Start training with smaller datasets and find models that are viable at that size. Once a reasonable performance is reached for that smaller dataset expand to the larger and start to optimize for that total dataset. 


How to Run:
The training of these networks was performed using the Aurora cluster at LUNARC but can of course be performed locally using data generated by the user. For now it will be assumed that the training is to use Aurora for the training. Currently the different datasets with events with up to four electrons are stored in the following directories on Aurora:

- [ ] /projects/hep/fs9/shared/ldmx/ldcs/gridftp/mc23/v14/4.0GeV/v3.2.2-1e-v14
- [ ] /projects/hep/fs9/shared/ldmx/ldcs/gridftp/mc23/v14/4.0GeV/v3.2.2-2e-v14 
- [ ] /projects/hep/fs9/shared/ldmx/ldcs/gridftp/mc23/v14/4.0GeV/v3.2.2-3e-v14
- [ ] /projects/hep/fs9/shared/ldmx/ldcs/gridftp/mc23/v14/4.0GeV/v3.2.2-4e-v14

Since four different types of neural networks were considered for this project the data needs to be preprocessed four times. The different preprocessing files can be found in the folders: CNN and Combine-PreProcessing for the CNN and Combined CNN and RNN model, GNN-PreProcessing for the GNN model, and RNN-PreProcessing for the RNN model. Each folder contains 1e, 2e, 3e, and 4e subfolders that contain preprocessing files for each type of event. In order to start we do:
1. If the data already on Aurora is used then get the list of file names from each directory into a series of .csv files 
2. Look at the DataExtractor.py file and replace all of the directory file names with the actual directory being worked in and run the file for each list and each multiplicity of the event. This should yield a series of files such as EcalID and Energy files for each multiplicity.  In order to submit the different tasks to Aurora the AuriraJobEx.sh file contains a basic version of a job submission. Change the python file name to the file considered and submit a job with: sbatch AuroraJobEx.sh, this also assumes that the .sh file has been compiled before submitting the job.
3. The folder named Trigger Scintillator contains files that will turn the positional data from the Trigger Scintillator into module and cell models that can then be used during the preprocessing. One is used for each multiplicity such that it gives four separate files that can then be combined with the other data.
4. The 1e pre processing files have documentation outlining how they work but they all need to have the directory specified. One method for saving the files would be to ensure that they are saved to Ecal, ETS (Ecal and Trigger Scintillator), and ETSX(Ecal and modified Trigger Scintillator) folders. These jobs work well on the cluster and will require 36 different files to run properly. 
5. Once the pre processing is done the data is ready for the models to use. Each model file requires adding details about the exact directory being used for the files. When preparing the script for submitting the job increasing the number of nodes was found to have benefits especially for the CNN type of models. The versions included in the models are for the ETS/ETSX types of datasets but can easily be modified to deal with the other types. This can then be used to start training the models.


Required Modules:
- [ ] Uproot
- [ ] Pandas 
- [ ] Numpy 
- [ ] Tensorflow 
- [ ] Pytorch Geometric 
- [ ] Networkx
- [ ] Sklearn 


