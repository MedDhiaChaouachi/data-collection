import React, { useState } from "react";
import { Link, Navigate } from "react-router-dom"; // Import Navigate
import { connect } from "react-redux";
import { login } from "../actions/auth";
import axios from "axios";
import "../css/app.css";

const Login = ({ login, isAuthenticated }) => {
  const [formData, setFormData] = useState({
    email: "",
    password: "",
  });

  const { email, password } = formData;

  const onChange = (e) =>
    setFormData({ ...formData, [e.target.name]: e.target.value });

  const onSubmit = (e) => {
    e.preventDefault();

    login(email, password);
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
        <h1>Sign In</h1> {/* Change to match heading of second login page */}
        <p>Sign into your Account</p>{" "}
        {/* Change to match paragraph of second login page */}
        <form onSubmit={(e) => onSubmit(e)}>
          <div className="cont2">
            {" "}
            {/* Use class from second login page */}
            <input
              className="form-control"
              type="email"
              placeholder="Email"
              name="email"
              value={email}
              onChange={(e) => onChange(e)}
              required
            />
            <input
              className="form-control"
              type="password"
              placeholder="Password"
              name="password"
              value={password}
              onChange={(e) => onChange(e)}
              minLength="6"
              required
            />
            <input type="submit" value="Login" className="button" />{" "}
            {/* Use button class from second login page */}
          </div>
        </form>
        <br />
        <p className="mt-3">
          Don't have an account? <Link to="/signup">Sign Up</Link>
        </p>
        <p className="mt-3">
          Forgot your Password? <Link to="/reset-password">Reset Password</Link>
        </p>
      </div>
    </div>
  );
};

const mapStateToProps = (state) => ({
  isAuthenticated: state.auth.isAuthenticated,
});

export default connect(mapStateToProps, { login })(Login);
