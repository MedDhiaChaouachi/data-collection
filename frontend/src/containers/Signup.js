import React, { useState } from "react";
import { Link, Navigate } from "react-router-dom"; // Import Navigate
import { connect } from "react-redux";
import { signup } from "../actions/auth";
import axios from "axios";
import "../css/app.css";

const Signup = ({ signup, isAuthenticated }) => {
  const [accountCreated, setAccountCreated] = useState(false);
  const [formData, setFormData] = useState({
    first_name: "",
    last_name: "",
    email: "",
    password: "",
    re_password: "",
  });

  const { first_name, last_name, email, password, re_password } = formData;

  const onChange = (e) =>
    setFormData({ ...formData, [e.target.name]: e.target.value });

  const onSubmit = async (e) => {
    e.preventDefault();

    if (password === re_password) {
      await signup(first_name, last_name, email, password, re_password);
      setAccountCreated(true);
    }
  };

  const continueWithGoogle = async () => {
    try {
      const res = await axios.get(
        `${process.env.REACT_APP_API_URL}/auth/o/google-oauth2/?redirect_uri=${process.env.REACT_APP_API_URL}/google`
      );

      window.location.replace(res.data.authorization_url);
    } catch (err) {}
  };

  const continueWithFacebook = async () => {
    try {
      const res = await axios.get(
        `${process.env.REACT_APP_API_URL}/auth/o/facebook/?redirect_uri=${process.env.REACT_APP_API_URL}/facebook`
      );

      window.location.replace(res.data.authorization_url);
    } catch (err) {}
  };

  if (isAuthenticated) {
    return <Navigate to="/" />; // Use Navigate
  }
  if (accountCreated) {
    return <Navigate to="/login" />; // Use Navigate
  }

  return (
    <div className="App">
      <div className="left">
        <div className="title-container">
          <h2>Analytica choose your right Business</h2>
        </div>
      </div>

      <div className="right">
        {" "}
        {/* Add right div */}
        <div className="container mt-5">
          <h1>Sign Up</h1>
          <p>Create your Account</p>
          <form onSubmit={(e) => onSubmit(e)}>
            <div className="form-group">
              <input
                className="form-control"
                type="text"
                placeholder="First Name*"
                name="first_name"
                value={first_name}
                onChange={(e) => onChange(e)}
                required
              />
            </div>
            <div className="form-group">
              <input
                className="form-control"
                type="text"
                placeholder="Last Name*"
                name="last_name"
                value={last_name}
                onChange={(e) => onChange(e)}
                required
              />
            </div>
            <div className="form-group">
              <input
                className="form-control"
                type="email"
                placeholder="Email*"
                name="email"
                value={email}
                onChange={(e) => onChange(e)}
                required
              />
            </div>
            <div className="form-group">
              <input
                className="form-control"
                type="password"
                placeholder="Password*"
                name="password"
                value={password}
                onChange={(e) => onChange(e)}
                minLength="6"
                required
              />
            </div>
            <div className="form-group">
              <input
                className="form-control"
                type="password"
                placeholder="Confirm Password*"
                name="re_password"
                value={re_password}
                onChange={(e) => onChange(e)}
                minLength="6"
                required
              />
            </div>
            <button className="btn btn-primary" type="submit">
              Register
            </button>
          </form>
          <br />

          <p className="mt-3">
            Already have an account? <Link to="/login">Sign In</Link>
          </p>
        </div>
      </div>
    </div>
  );
};

const mapStateToProps = (state) => ({
  isAuthenticated: state.auth.isAuthenticated,
});

export default connect(mapStateToProps, { signup })(Signup);
