from pyspark.sql import SparkSession
from initializer_customer import load_customer_profile


def main():

    spark = (
        SparkSession.builder
        .appName("CustomerProfileApp")
        .getOrCreate()
    )

    # Get DataFrame from initializer
    customer_df = load_customer_profile(spark)

    print("Customer Data:")
    customer_df.show(truncate=False)

    print("Gold Customers:")
    customer_df.filter(
        customer_df.loyalty_tier == "Gold"
    ).show(truncate=False)

    spark.stop()


if __name__ == "__main__":
    main()
