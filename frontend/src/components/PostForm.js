import React, { useState } from "react";
import "../css/styles.css"; // Import the CSS file
import axios from "axios";

function CreatePost() {
  const [formData, setFormData] = useState({
    title: "",
    text: "",
    category: "",
    image: null,
  });

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleImageChange = (e) => {
    setFormData({ ...formData, image: e.target.files[0] });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    const accessToken = localStorage.getItem("accessToken"); // Retrieve accessToken from local storage
    if (!accessToken) {
      console.error("Access token is missing.");
      return;
    }

    const postData = new FormData();
    postData.append("title", formData.title);
    postData.append("text", formData.text);
    postData.append("category", formData.category);
    postData.append("image", formData.image);

    try {
      const response = await axios.post(
        "http://localhost:8000/create_post",
        postData,
        {
          headers: {
            Authorization: `Bearer ${accessToken}`, // Include authentication token
            "Content-Type": "application/json",
          },
        }
      );
      console.log(response.data);
      // Handle success
    } catch (error) {
      console.error("Error creating post:", error);
      // Handle error
    }
  };

  return (
    <div>
      <h1>Create Post</h1>
      <form onSubmit={handleSubmit}>
        <div>
          <label>Title:</label>
          <input
            type="text"
            name="title"
            value={formData.title}
            onChange={handleChange}
            required
          />
        </div>
        <div>
          <label>Text:</label>
          <textarea
            name="text"
            value={formData.text}
            onChange={handleChange}
            required
          />
        </div>
        <div>
          <label>Category:</label>
          <select
            name="category"
            value={formData.category}
            onChange={handleChange}
            required
          >
            <option value="">Select category</option>
            <option value="math">Math</option>
            <option value="philosophy">Philosophy</option>
            <option value="science">Science</option>
            <option value="political">Political</option>
            <option value="other">Other</option>
          </select>
        </div>
        <div>
          <label>Image:</label>
          <input
            type="file"
            name="image"
            onChange={handleImageChange}
            accept="image/*"
          />
        </div>
        <button type="submit">Create Post</button>
      </form>
    </div>
  );
}

export default CreatePost;
