import axios from "axios"
import { useState } from "react"

interface QueryResponse {
  answer: string
}

export default function Query() {
  const [question, setQuestion] = useState<string>("")
  const [answer, setAnswer] = useState<string>("")
  const [loading, setLoading] = useState<boolean>(false)

  const handleAsk = async () => {
    if (!question.trim()) return

    try {
      setLoading(true)

      const res = await axios.post<QueryResponse>(
        "http://127.0.0.1:8000/api/query",
        { question }
      )

      setAnswer(JSON.stringify(res.data))
    } catch (error) {
      console.error(error)
      alert("Failed to generate answer")
    } finally {
      setLoading(false)
    }
  }

  return (
    <div>
      <textarea
        className="w-full p-3 border rounded"
        placeholder="Ask a law question..."
        value={question}
        onChange={(e) => setQuestion(e.target.value)}
      />

      <button
        onClick={handleAsk}
        disabled={loading}
        className="mt-3 px-4 py-2 bg-green-600 text-white rounded disabled:opacity-50"
      >
        {loading ? "Generating..." : "Generate Answer"}
      </button>

      <div className="mt-6 whitespace-pre-wrap bg-white p-4 rounded shadow">
        {answer}
      </div>
    </div>
  )
}
