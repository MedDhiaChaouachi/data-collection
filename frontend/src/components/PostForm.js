import React, { useState } from "react";
import "../css/styles.css"; // Import the CSS file

function CreatePost() {
  const [title, setTitle] = useState("");
  const [text, setText] = useState("");
  const [category, setCategory] = useState("");
  const [author, setAuthor] = useState("");
  const [images, setImages] = useState([]);

  const handleSubmit = async (e) => {
    e.preventDefault();

    // Form data to be sent to the server
    const formData = {
      title,
      text,
      category,
      author,
      images,
    };

    // Send form data to the server
    try {
      const response = await fetch("/create_post", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(formData),
      });

      if (response.ok) {
        console.log("Post created successfully");
        // Reset form fields
        setTitle("");
        setText("");
        setCategory("");
        setAuthor("");
        setImages([]);
      } else {
        console.error("Failed to create post");
      }
    } catch (error) {
      console.error("Error:", error);
    }
  };

  const handleImageChange = (e) => {
    const files = e.target.files;
    setImages(files);
  };

  return (
    <div className="post-form-container">
      <h1>Create a New Post</h1>
      <h6 className="instruction">
        Fill out the form below to publish a new post.
      </h6>
      <form className="post-form" onSubmit={handleSubmit}>
        <div>
          <label>Title:</label>
          <input
            type="text"
            value={title}
            onChange={(e) => setTitle(e.target.value)}
            placeholder="Enter a title"
          />
        </div>

        <div>
          <label>Text:</label>
          <textarea
            className="textareaa"
            value={text}
            onChange={(e) => setText(e.target.value)}
            placeholder="Write your post content"
          ></textarea>
        </div>

        <div>
          <label>Category:</label>
          <select
            value={category}
            onChange={(e) => setCategory(e.target.value)}
          >
            <option value="math">Math</option>
            <option value="philosophy">Philosophy</option>
            <option value="science">Science</option>
            <option value="political">Political</option>
            <option value="other">Other</option>
          </select>
        </div>

        <div>
          <label>Author:</label>
          <input
            type="text"
            value={author}
            onChange={(e) => setAuthor(e.target.value)}
            placeholder="Enter the author's name"
          />
        </div>

        <div>
          <label>Images:</label>
          <input type="file" multiple onChange={handleImageChange} />
        </div>

        <button type="submit">Publish Post</button>
      </form>
    </div>
  );
}

export default CreatePost;
