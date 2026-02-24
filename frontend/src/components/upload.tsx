import axios from "axios"
import { useState, ChangeEvent } from "react"

export default function Upload() {
  const [file, setFile] = useState<File | null>(null)
  const [loading, setLoading] = useState<boolean>(false)

  const handleUpload = async () => {
    if (!file) return

    try {
      setLoading(true)

      const formData = new FormData()
      formData.append("file", file)

      await axios.post(
        "http://127.0.0.1:8000/api/upload",
        formData,
        {
          headers: {
            "Content-Type": "multipart/form-data"
          }
        }
      )

      alert("Uploaded Successfully")
    } catch (error) {
      console.error(error)
      alert("Upload failed")
    } finally {
      setLoading(false)
    }
  }

  const handleFileChange = (e: ChangeEvent<HTMLInputElement>) => {
    if (e.target.files && e.target.files.length > 0) {
      setFile(e.target.files[0])
    }
  }

  return (
    <div className="mb-8">
      <input
        type="file"
        onChange={handleFileChange}
      />

      <button
        onClick={handleUpload}
        disabled={loading}
        className="ml-4 px-4 py-2 bg-blue-600 text-white rounded disabled:opacity-50"
      >
        {loading ? "Uploading..." : "Upload PDF"}
      </button>
    </div>
  )
}
