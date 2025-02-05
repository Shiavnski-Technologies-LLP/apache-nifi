# *NiFi Data Processing 📝🔄*

This project automates the process of capitalizing a specific column in a CSV file using **Apache NiFi** and a **Python script**. 🐍📊

---

## 📂 Project Structure

- **📁 data/**: Contains input and processed CSV files.
- **📁 nifi-flows/**: Includes NiFi configurations for data processing.
- **📁 scripts/**: Contains the Python script for data transformation.
- **📁 database/**: Stores database configurations.

---

## 🚀 Steps to Run the Project

### 1️⃣ Setup NiFi

#### 1️⃣ Install Apache NiFi ⚙️

Ensure that **Apache NiFi** is installed on your machine. You can download it from the [official website](https://nifi.apache.org/download.html).

#### 2️⃣ Import the NiFi Flow Template

- Import the **flow-template.xml** into NiFi to get the pre-configured data flow.

---

### 2️⃣ Configure NiFi Processors

To automate the data transformation, configure the following processors in NiFi:

- **🛠️ GetFile Processor**: Reads the input CSV file from the `data/input/` folder. 📂
- **🛠️ ExecuteScript Processor**: Runs the Python script to capitalize a specific column in the CSV file. 🔠
- **🛠️ PutDatabaseRecord Processor**: Stores the transformed data in your database. 🗄️
- **🛠️ LogMessage Processor**: Logs the processing details for debugging and monitoring. 📝

---

### 3️⃣ Running the Process

Follow these steps to run the NiFi data flow:

- ✔️ **Start Apache NiFi**: Launch NiFi to begin processing.
- ✔️ **Upload a Sample CSV**: Place the CSV file in the `data/input/` folder.
- ✔️ **Monitor the Flow**: Watch the process run and check the results in:
    - **Output Folder**: `data/output/`
    - **Database**: Ensure data has been correctly stored.

---

## 💡 Tips

- 🔧 **Database Connection**: Before running the flow, verify that your **database connection settings** are correct to avoid errors during processing. 🛠️🔥

---

## 📄 License 📝

This project is licensed under the **MIT License**. See the LICENSE file for details.
