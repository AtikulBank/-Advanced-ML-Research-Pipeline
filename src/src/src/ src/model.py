from xgboost import XGBRegressor

def get_model(config):
    return XGBRegressor(
        n_estimators=config["model"]["n_estimators"],
        max_depth=config["model"]["max_depth"],
        learning_rate=config["model"]["learning_rate"]
    )
