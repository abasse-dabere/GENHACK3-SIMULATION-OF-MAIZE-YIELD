#############################################################################
# YOUR GENERATIVE MODEL
# ---------------------
# Should be implemented in the 'generative_model' function
# !! *DO NOT MODIFY THE NAME OF THE FUNCTION* !!
#
# You can store your parameters in any format you want (npy, h5, json, yaml, ...)
# <!> *SAVE YOUR PARAMETERS IN THE parameters/ DICRECTORY* <!>
#
# See below an example of a generative model
# Z,x |-> G_\theta(Z,x)
############################################################################

# <!> DO NOT ADD ANY OTHER ARGUMENTS <!>

from tensorflow.keras.models import load_model
import numpy as np
import joblib

def generative_model(noise, scenario):
    """
    Generative model

    Parameters
    ----------
    noise : ndarray with shape (n_samples, n_dim=4)
        input noise of the generative model
    scenario: ndarray with shape (n_samples, n_scenarios=9)
        input categorical variable of the conditional generative model
    """
    # See below an example
    # ---------------------
    latent_dim = 50
    latent_variable = noise[:, :latent_dim]  # choose the appropriate latent dimension of your model

    # load your parameters or your model
    # <!> be sure that they are stored in the parameters/ directory <!>
    model_1 = load_model("parameters/scenario_1_gen.h5")  # load model for scenario 1
    scaler_1 = joblib.load('parameters/scenario_1_scaler.joblib') # load scaler for scenario 1

    model_2 = load_model("parameters/scenario_2_gen.h5")  # load model for scenario 2
    scaler_2 = joblib.load('parameters/scenario_2_scaler.joblib') # load scaler for scenario 2

    model_3 = load_model("parameters/scenario_3_gen.h5")  # load model for scenario 3
    scaler_3 = joblib.load('parameters/scenario_3_scaler.joblib') # load scaler for scenario 3

    model_4 = load_model("parameters/scenario_4_gen.h5")  # load model for scenario 4
    scaler_4 = joblib.load('parameters/scenario_4_scaler.joblib') # load scaler for scenario 4

    model_5 = load_model("parameters/scenario_5_gen.h5")  # load model for scenario 5
    scaler_5 = joblib.load('parameters/scenario_5_scaler.joblib') # load scaler for scenario 5

    model_6 = load_model("parameters/scenario_6_gen.h5")  # load model for scenario 6
    scaler_6 = joblib.load('parameters/scenario_6_scaler.joblib') # load scaler for scenario 6

    model_7 = load_model("parameters/scenario_7_gen.h5")  # load model for scenario 7
    scaler_7 = joblib.load('parameters/scenario_7_scaler.joblib') # load scaler for scenario 7

    model_8 = load_model("parameters/scenario_8_gen.h5")  # load model for scenario 8
    scaler_8 = joblib.load('parameters/scenario_8_scaler.joblib') # load scaler for scenario 8

    model_9 = load_model("parameters/scenario_9_gen.h5")  # load model for scenario 9
    scaler_9 = joblib.load('parameters/scenario_9_scaler.joblib') # load scaler for scenario 9

    outputs = np.zeros((noise.shape[0], 4))
    for scen in range(1, 10):
        mask = scenario[:, scen-1] == 1
        if scen == 1:
            outputs[mask] = scaler_1.inverse_transform(model_1.predict(latent_variable[mask]))
        elif scen == 2:
            outputs[mask] = scaler_2.inverse_transform(model_2.predict(latent_variable[mask]))
        elif scen == 3:
            outputs[mask] = scaler_3.inverse_transform(model_3.predict(latent_variable[mask]))
        elif scen == 4:
            outputs[mask] = scaler_4.inverse_transform(model_4.predict(latent_variable[mask]))
        elif scen == 5:
            outputs[mask] = scaler_5.inverse_transform(model_5.predict(latent_variable[mask]))
        elif scen == 6:
            outputs[mask] = scaler_6.inverse_transform(model_6.predict(latent_variable[mask]))
        elif scen == 7:
            outputs[mask] = scaler_7.inverse_transform(model_7.predict(latent_variable[mask]))
        elif scen == 8:
            outputs[mask] = scaler_8.inverse_transform(model_8.predict(latent_variable[mask]))
        elif scen == 9:
            outputs[mask] = scaler_9.inverse_transform(model_9.predict(latent_variable[mask]))

    return outputs # G(Z)
    # return model(latent_variable, scenario) # G(Z, x)




