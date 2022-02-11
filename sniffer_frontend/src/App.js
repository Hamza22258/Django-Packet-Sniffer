import { useState, useEffect } from "react";
import axios from "axios";
import MaterialTable from "material-table";
import { Button } from "@material-ui/core";
import "./app.css";
function App() {
  var cond = true;
  const [start, setStart] = useState(0);
  const [data, setDataVar] = useState("");
  const [packets, setPackets] = useState([]);
  useEffect(() => {
    axios
      .get("http://127.0.0.1:8000/api/getPackets/")
      .then((res) => setPackets(res.data));
  }, []);
  return (
    <div style={{ maxWidth: "100%" }}>
      <Button
        variant="outlined"
        onClick={(e) => {
          axios
            .post("http://127.0.0.1:8000/api/start/", { data1: 0 })
            .then((res) => (window.location.href = ""));
        }}
      >
        Start
      </Button>
      <Button
        variant="outlined"
        onClick={(e) => {
          axios
            .post("http://127.0.0.1:8000/api/stop/", { data1: 1 })
            .then((res) => {
              window.location.href = "";
              console.log(res);
            });
        }}
      >
        Stop
      </Button>
      <Button
        variant="outlined"
        onClick={(e) => {
          axios
            .post("http://127.0.0.1:8000/api/delete/", { data })
            .then((res) => (window.location.href = ""));
        }}
      >
        Delete
      </Button>
      <MaterialTable
        columns={[
          { title: "Packet", field: "packet_type" },
          {
            title: "Src Port",
            field: "src_port",
          },
          {
            title: "Dest Port",
            field: "dest_port",
          },
          { title: "SrcIP", field: "src_IP" },
          { title: "DestIP", field: "dest_IP" },

          {
            title: "Data",
            field: "data",
            render: (rowData) => (
              <Button
                className="btn"
                id={rowData.id}
                variant="outlined"
                onClick={(e) => {
                  if (cond == true) {
                    if (rowData.data == "") {
                      document.getElementById(rowData.id).innerText = "No Data";
                    } else {
                      document.getElementById(rowData.id).innerText =
                        rowData.data;
                    }
                    setDataVar(rowData.data);
                    cond = false;
                  } else {
                    document.getElementById(rowData.id).innerText = "Data";
                    setDataVar("");
                    cond = true;
                  }
                }}
              >
                Data
              </Button>
            ),
          },
        ]}
        data={packets}
        title="Packets"
      />
    </div>
  );
}

export default App;
function DisplayData(props) {
  return (
    <div class="card">
      <div class="container">
        <p>{props.data}</p>
      </div>
    </div>
  );
}
