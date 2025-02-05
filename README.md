
## **NiFi Data Processing 📝🔄

This project automates the process of capitalizing a specific column in a CSV file using **Apache NiFi** and a **Python script**. 🐍📊

## **📂 Project Structure**

📁 `data/` - Contains input and processed CSV files.  
📁 `nifi-flows/` - Includes NiFi configurations for data processing.  
📁 `scripts/` - Contains the Python script for data transformation.  
📁 `database/` - Stores database configurations.

## **🚀 Steps to Run the Project**

### **1️⃣ Setup NiFi**

1️⃣ Install [Apache NiFi](https://nifi.apache.org/) ⚙️  
2️⃣ Import `flow-template.xml` into NiFi

### **2️⃣ Configure Processors**

🛠️ **GetFile Processor** - Reads the input CSV file 📂  
🛠️ **ExecuteScript Processor** - Runs Python script to capitalize a column 🔠  
🛠️ **PutDatabaseRecord Processor** - Stores transformed data in the database 🗄️  
🛠️ **LogMessage Processor** - Logs processing details for debugging 📝

### **3️⃣ Running the Process**

✔️ Start Apache NiFi  
✔️ Upload a sample CSV file to the `data/input/` folder  
✔️ Monitor the flow and verify results in `data/output/` and the database

---

💡 **Tip:** Make sure your database connection settings are correct before running the process. 🛠️🔥

---

📄 License 📝
This project is licensed under the MIT License. See the LICENSE file for details.
