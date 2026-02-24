import Upload from "./components/Upload"
import Query from "./components/Query"

function App() {
  return (
    <div className="min-h-screen bg-gray-100 p-10">
      <h1 className="text-3xl font-bold mb-6">
        LLB Study Hub
      </h1>

      <Upload />
      <Query />
    </div>
  )
}

export default App
