// src/components/SubmitRecipe.tsx
import React, { useState } from "react";
import axios from "axios";
import { RecipeCreate } from "../types/recipe";
import { useNavigate } from "react-router-dom";

export default function SubmitRecipe() {
  const [form, setForm] = useState<RecipeCreate>({
    title: "",
    description: "",
    ingredients: "",
    steps: "",
    tags: "",
    image: "",
  });
  const [file, setFile] = useState<File | null>(null);
  const [preview, setPreview] = useState<string | null>(null);

  const navigate = useNavigate();

  const handleChange = (
    e: React.ChangeEvent<HTMLInputElement | HTMLTextAreaElement>
  ) => {
    setForm({ ...form, [e.target.name]: e.target.value });
  };

  const handleFileChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    if (e.target.files && e.target.files[0]) {
      setFile(e.target.files[0]);
      setPreview(URL.createObjectURL(e.target.files[0]));
    }
  };

  const submit = async (e: React.FormEvent) => {
    e.preventDefault();

    try {
      let imagePath = form.image;

      if (file) {
        const formData = new FormData();
        formData.append("file", file);

        // Upload image to backend
        const uploadRes = await axios.post(
          "http://localhost:8000/recipes/upload",
          formData,
          { headers: { "Content-Type": "multipart/form-data" } }
        );

        imagePath = uploadRes.data.url; // backend returns uploaded file path
      }

      // Submit recipe
      const res = await axios.post("http://localhost:8000/recipes/", {
        ...form,
        image: imagePath,
      });

      alert("Recipe submitted successfully!");
      navigate(`/recipes/${res.data.id}`);
    } catch (err) {
      console.error(err);
      alert("Error submitting recipe");
    }
  };

  return (
    <form
      onSubmit={submit}
      className="max-w-lg mx-auto p-6 bg-white rounded shadow"
    >
      <h2 className="text-2xl font-semibold mb-4">Submit a Recipe</h2>

      <input
        name="title"
        placeholder="Title"
        value={form.title}
        onChange={handleChange}
        className="w-full border p-2 mb-3 rounded"
      />

      <textarea
        name="description"
        placeholder="Description"
        value={form.description}
        onChange={handleChange}
        className="w-full border p-2 mb-3 rounded"
      />

      <textarea
        name="ingredients"
        placeholder="Ingredients (one per line)"
        value={form.ingredients}
        onChange={handleChange}
        className="w-full border p-2 mb-3 rounded"
      />

      <textarea
        name="steps"
        placeholder="Steps"
        value={form.steps}
        onChange={handleChange}
        className="w-full border p-2 mb-3 rounded"
      />

      <input
        name="tags"
        placeholder="Tags (comma separated)"
        value={form.tags}
        onChange={handleChange}
        className="w-full border p-2 mb-3 rounded"
      />

      <div className="mb-3">
        <label className="block mb-1 font-medium">Upload Image:</label>
        <input type="file" accept="image/*" onChange={handleFileChange} />
        {preview && (
          <img
            src={preview}
            alt="Preview"
            className="mt-2 w-full h-48 object-cover rounded"
          />
        )}
      </div>

      <div className="flex justify-end">
        <button
          type="submit"
          className="bg-green-500 text-white px-4 py-2 rounded hover:bg-green-600"
        >
          Submit
        </button>
      </div>
    </form>
  );
}
