from pyspark.sql import SparkSession


def load_customer_profile(spark):
    """
    Creates and returns customer profile DataFrame
    """

    customer_data = [
        ("CUS1-001", "Alice Johnson", "alice@example.com", "555-1111", "Gold"),
        ("CUS1-002", "Brian Smith", "brian@example.com", "555-2222", "Silver"),
        ("CUS1-003", "Carla Gomez", "carla@example.com", "555-3333", "Bronze")
    ]

    columns = [
        "customer_id",
        "name",
        "email",
        "phone",
        "loyalty_tier"
    ]

    customer_df = spark.createDataFrame(customer_data, columns)

    return customer_df