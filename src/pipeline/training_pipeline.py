from src.components.data_ingestion import DataIngestion
from src.components.data_transformation import DataTransformation
from src.components.model_trainer import ModelTrainer


if __name__ == "__main__":
    obj = DataIngestion()
    train_data_path, test_data_path = obj.start_data_ingestion()

    data_transformation = DataTransformation()
    train_arr, test_arr, _ = data_transformation.start_data_transformation(train_data_path, test_data_path)
    
    model_training = ModelTrainer()
    model_training.start_model_trainer(train_arr, test_arr)