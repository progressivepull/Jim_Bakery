# Jim_Bakery

# PySpark Setup Verification

The following steps verify that PySpark is installed and working correctly on Windows using Git Bash.

## 1. Activate the Virtual Environment

```bash
source /d/GitHubProgressivePull/Jim_Bakery/venv2/Scripts/activate
```

Verify the environment is active:

```bash
pip list
```

Expected output:

```text
Package Version
------- --------
pip     26.1.2
py4j    0.10.9.9
pyspark 4.2.0
```

---

## 2. Verify Java Installation

Check the installed Java version:

```bash
java -version
```

Expected output:

```text
java version "17.0.12" 2024-07-16 LTS
Java(TM) SE Runtime Environment (build 17.0.12+8-LTS-286)
Java HotSpot(TM) 64-Bit Server VM (build 17.0.12+8-LTS-286, mixed mode, sharing)
```

Find the Java executable:

```bash
which java
```

Expected output:

```text
/c/Program Files/Java/jdk-17/bin/java
```

---

## 3. Run the PySpark Application

Execute the application:

```bash
python ./main_customer.py
```

Sample output:

```text
Customer Data:

+-----------+-------------+-----------------+--------+------------+
|customer_id|name         |email            |phone   |loyalty_tier|
+-----------+-------------+-----------------+--------+------------+
|CUS1-001   |Alice Johnson|alice@example.com|555-1111|Gold        |
|CUS1-002   |Brian Smith  |brian@example.com|555-2222|Silver      |
|CUS1-003   |Carla Gomez  |carla@example.com|555-3333|Bronze      |
+-----------+-------------+-----------------+--------+------------+

Gold Customers:

+-----------+-------------+-----------------+--------+------------+
|customer_id|name         |email            |phone   |loyalty_tier|
+-----------+-------------+-----------------+--------+------------+
|CUS1-001   |Alice Johnson|alice@example.com|555-1111|Gold        |
+-----------+-------------+-----------------+--------+------------+
```

---

## 4. Understanding the Warnings

You may see warnings such as:

```text
WARN Shell: Did not find winutils.exe
```

and

```text
WARN NativeCodeLoader:
Unable to load native-hadoop library for your platform
```

These warnings are common when running PySpark on Windows and can usually be ignored for local development and testing.

Since the application successfully:

- Creates a Spark session
- Loads data
- Creates a DataFrame
- Executes transformations
- Displays results using `df.show()`

your PySpark installation is functioning correctly.

---

## 5. Example: Using `df.show()`

Create a simple DataFrame and display it:

```python
from pyspark.sql import SparkSession

spark = (
    SparkSession.builder
    .appName("TestApp")
    .master("local[*]")
    .getOrCreate()
)

data = [
    ("Alice", 25),
    ("Bob", 30),
    ("Charlie", 35)
]

df = spark.createDataFrame(data, ["name", "age"])

df.show()

spark.stop()
```

Expected output:

```text
+-------+---+
|   name|age|
+-------+---+
|  Alice| 25|
|    Bob| 30|
|Charlie| 35|
+-------+---+
```

---

## 6. Useful DataFrame Commands

### Display Rows

```python
df.show()
```

### Display First 5 Rows

```python
df.show(5)
```

### Display Without Truncation

```python
df.show(truncate=False)
```

### Display Schema

```python
df.printSchema()
```

### Display Column Names

```python
print(df.columns)
```

### Count Rows

```python
print(df.count())
```

---

## 7. Start an Interactive PySpark Shell

Launch PySpark:

```bash
pyspark
```

Create and display a DataFrame:

```python
df = spark.createDataFrame(
    [("Alice", 25), ("Bob", 30)],
    ["name", "age"]
)

df.show()
```

Expected output:

```text
+-----+---+
| name|age|
+-----+---+
|Alice| 25|
|  Bob| 30|
+-----+---+
```

---

## Verification Summary

✅ Virtual environment activated

✅ PySpark 4.2.0 installed

✅ Java 17 detected

✅ Spark session created successfully

✅ DataFrame operations working

✅ `df.show()` displaying results correctly

✅ Local PySpark development environment ready for use