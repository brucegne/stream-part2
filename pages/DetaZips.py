import streamlit as st
from deta import Deta

# Connect to Deta Base with your Data Key
deta = Deta("b0fhjqxu_fG4y33DEMaK8qWfMGABUSbn8cGFNxXhC")

# Create a new database "example-db"
# If you need a new database, just use another name.
db = deta.Base("Zipcode")
"---"
"Here's everything stored in the database:"
"---"
county="Johnson"
state = "NE"
qryString = str({"county?contains": "%s", "state": "%s"}) % (county, state)
st.write(qryString)
db_content = db.fetch({'county?contains': 'Johnson', 'state': 'NE'}).items
st.dataframe(db_content)

# If the user clicked the submit button,
# write the data from the form to the database.
# You can store any data you want here. Just modify that dictionary below (the entries between the {}).
# st.write(db_content)