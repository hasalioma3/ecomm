import React from "react";
import { Spinner } from "react-bootstrap";
function Loader() {
  return (
    <Spinner
      animation="border"
      role="status"
      style={{
        height: "200px",
        width: "200px",
        margin: "auto",
        display: "block",
      }}
    >
      <span className="sr-only">Loading...</span>
    </Spinner>
  );
}

export default Loader;
