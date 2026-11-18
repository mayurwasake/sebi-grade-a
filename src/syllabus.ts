export type SyllabusTopic = { title: string; details: string[]; weight?: string }
export type SyllabusPaper = { title: string; note: string; topics: SyllabusTopic[] }
export const syllabusSource = 'https://www.sebi.gov.in/sebi_data/careerfiles/oct-2025/1761782417659.pdf'

export const syllabus: Record<string, SyllabusPaper[]> = {
  'Phase 1': [
    { title: 'Paper 1 · Common', note: 'Multiple choice · 100 marks · 60 minutes', topics: [
      { title: 'General Awareness', details: ['Financial sector awareness (easy to moderate difficulty)'] },
      { title: 'English Language', details: ['English language questions'] },
      { title: 'Quantitative Aptitude', details: ['Quantitative aptitude questions'] },
      { title: 'Test of Reasoning', details: ['Reasoning ability questions'] },
    ] },
    { title: 'Paper 2 · Information Technology', note: 'Multiple choice · 100 marks · 40 minutes', topics: [
      { title: 'Database Concepts', weight: '10%', details: ['ER model', 'Relational model: relational algebra and tuple calculus', 'Integrity constraints and normal forms', 'File organization', 'Indexing, including B and B+ trees', 'Transactions and concurrency control'] },
      { title: 'SQL Queries', weight: '10%', details: ['SELECT, VIEW, TRUNCATE, DELETE, UPDATE and ALTER', 'INNER JOIN and types of OUTER JOIN', 'Aggregate functions', 'UNION, INTERSECTION and EXCEPT', 'IN and EXISTS clauses', 'Nested queries'] },
      { title: 'Programming Concepts (Java / C / C++)', weight: '30%', details: ['Program control: iteration, recursion and functions', 'Scope and binding of variables and functions', 'Parameter passing', 'Functional and logic programming', 'OOP concepts, inheritance, classes and objects', 'Constructors and functions', 'Exception handling'] },
      { title: 'Data Analytics Languages (Python / R)', weight: '10%', details: ['Regular expressions and slicing', 'Data reshaping and dataframes', 'Dictionaries, sets and lists', 'File management', 'Classes and functions', 'Data mining', 'Importing and exporting data', 'Charts and graphs'] },
      { title: 'Algorithms for Problem Solving', weight: '10%', details: ['Tree and graph traversals', 'Connected components, spanning trees and shortest paths', 'Hashing, sorting and searching', 'Greedy, dynamic programming and divide-and-conquer techniques'] },
      { title: 'Networking Concepts', weight: '10%', details: ['ISO/OSI stack', 'LAN technologies: Ethernet and Token Ring', 'TCP/UDP and IP', 'Switches, gateways and routers', 'DNS, SMTP, POP, FTP and HTTP', 'Firewalls'] },
      { title: 'Information & Cyber Security Concepts', weight: '10%', details: ['Cyber attacks', 'Software development security and network security', 'Authentication', 'CIA: confidentiality, integrity and availability', 'Network audit and systems audit'] },
      { title: 'Data Warehousing', weight: '5%', details: ['Data extraction, cleaning, transformation and loading', 'Metadata', 'Data cube and data mart', 'Data models'] },
      { title: 'Shell Programming', weight: '5%', details: ['Shell scripting basics', 'Shell variables and script arguments', 'If statements and loops', 'Return', 'Basic UNIX commands'] },
    ] },
  ],
  'Phase 2': [
    { title: 'Paper 1 · English (All streams)', note: 'Descriptive drafting skills · 100 marks · 60 minutes', topics: [
      { title: 'English Writing Skills', details: ['Essay writing', 'Precis writing', 'Comprehension', 'Expression and understanding of the topic'] },
    ] },
    { title: 'Paper 2 · Information Technology', note: 'MCQ · 100 marks · 180 minutes', topics: [
      { title: 'Algorithms', weight: '30%', details: ['Sorting and searching', 'Greedy algorithms', 'Dynamic programming', 'Backtracking', 'Divide and conquer', 'Pattern searching'] },
      { title: 'Data Structure', weight: '40%', details: ['Array and linked list', 'Stack and queue', 'Binary tree and binary search tree', 'Indexing and heap', 'Hashing', 'Matrix', 'JSON objects'] },
      { title: 'String Manipulation', weight: '10%', details: ['Length', 'Substring', 'Regular expressions', 'Search'] },
      { title: 'Object Oriented Programming', weight: '20%', details: ['Abstraction', 'Encapsulation', 'Polymorphism', 'Inheritance'] },
    ] },
  ],
}
