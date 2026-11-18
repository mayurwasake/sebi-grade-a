export type SyllabusDetail = { id: number; content: string; sort_order: number }
export type SyllabusTopic = { id: number; title: string; weightage: string | null; sort_order: number; details: SyllabusDetail[] }
export type SyllabusPaper = {
  id: number
  phase: string
  code: string
  title: string
  description: string
  duration_minutes: number | null
  max_marks: number | null
  sort_order: number
  topics: SyllabusTopic[]
}
export type SyllabusCycle = { id: number; year: number; stream: string; source_url: string; papers: SyllabusPaper[] }

const API_BASE_URL = import.meta.env.VITE_API_BASE_URL || 'http://localhost:8000/api/v1'

export async function getSyllabus(year: number, stream: string): Promise<SyllabusCycle> {
  const response = await fetch(`${API_BASE_URL}/syllabus/${year}/${encodeURIComponent(stream)}`)
  if (!response.ok) {
    if (response.status === 404) throw new Error(`No ${year} syllabus found for the ${stream} stream. Seed the syllabus catalog in the backend.`)
    throw new Error(`Syllabus request failed (${response.status}). Check that the API is running.`)
  }
  return response.json() as Promise<SyllabusCycle>
}
