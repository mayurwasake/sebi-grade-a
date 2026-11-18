# SEBI Prep OS

> A personal-first, structured and measurable preparation workspace for the SEBI Grade A examination.

SEBI Prep OS is a web application designed to help aspirants prepare consistently for the SEBI Grade A examination through structured learning, syllabus-wise coverage, practice assessments, revision, and progress tracking.

The goal is to create more than a collection of notes or a generic quiz application. We want to build a complete preparation environment that helps an aspirant understand concepts deeply, practise effectively, identify weaknesses, and maintain consistency throughout the preparation journey.

**Current Status:** Product planning and specification. The repository is currently at the documentation and foundation stage. The features and architecture described below represent the intended product, not already implemented functionality.

---

## Table of Contents

1. [Vision and Objectives](#1-vision-and-objectives)
2. [Product Principles](#2-product-principles)
3. [Target User and Scope](#3-target-user-and-scope)
4. [Examination and Syllabus Coverage](#4-examination-and-syllabus-coverage)
5. [Application Modules](#5-application-modules)
6. [Home Dashboard](#6-home-dashboard)
7. [Learning Workspace](#7-learning-workspace)
8. [Learning Content Standards](#8-learning-content-standards)
9. [Practice and Assessment Engine](#9-practice-and-assessment-engine)
10. [Revision Centre and Mistake Notebook](#10-revision-centre-and-mistake-notebook)
11. [Progress and Analytics](#11-progress-and-analytics)
12. [Study Consistency and Motivation](#12-study-consistency-and-motivation)
13. [Technical Stack](#13-technical-stack)
14. [Application Architecture](#14-application-architecture)
15. [Content and Database Architecture](#15-content-and-database-architecture)
16. [Security and Quality Requirements](#16-security-and-quality-requirements)
17. [Development Roadmap](#17-development-roadmap)
18. [MVP Acceptance Criteria](#18-mvp-acceptance-criteria)
19. [Future Scope](#19-future-scope)

---

# 1. Vision and Objectives

Build a personal preparation operating system that supports the complete SEBI Grade A preparation journey, from understanding the syllabus to revision and examination simulation.

The application should help the aspirant:

1. Understand what to study next without spending excessive time planning every session.
2. Learn every syllabus topic from fundamentals to examination-level depth.
3. Practise questions immediately after learning and after completing a topic.
4. Identify weak concepts and convert mistakes into revision actions.
5. Track actual learning activity, assessment performance, and retention separately.
6. Build a sustainable daily study habit through achievable goals and visible progress.
7. Prepare efficiently alongside professional and personal responsibilities.

### Core product objective

The application should answer three questions every day:

- What should I study today?
- Do I actually understand what I studied?
- What should I revise or improve next?

---

# 2. Product Principles

The application will follow these principles:

- **Learning before gamification:** Motivation features should support actual learning, not replace it.
- **Depth with clarity:** Explain concepts in simple language without sacrificing technical accuracy or important detail.
- **Syllabus traceability:** Every topic and module must map to a clearly identified syllabus area.
- **Practice integrated with learning:** Learners should be able to test understanding without leaving the learning workflow.
- **Honest progress tracking:** Opening a page is not equivalent to completing or mastering a topic.
- **Revision is essential:** Previously learned material and mistakes must return for revision.
- **Content independent of UI:** Learning content and questions must be stored as structured data, not hardcoded into React pages.
- **Incremental development:** Complete and test one functional part before expanding the application.
- **Maintainability:** Build reusable components and modular services rather than tightly coupled features.

---

# 3. Target User and Scope

### Initial target audience

Working professionals and serious aspirants preparing for SEBI Grade A who need a structured, consistent learning environment.

### Initial scope

- Individual/personal use.
- Phase-wise and subject-wise syllabus organization.
- Topic and module-based learning.
- Module-level knowledge checks.
- Topic-level assessments.
- Notes, bookmarks, and revision management.
- Mistake Notebook.
- Study-session tracking.
- Progress analytics and consistency tracking.

### Future scope

The architecture should be extensible to support multiple aspirants, shared question banks, community features, and additional examinations.

These are future possibilities, not requirements for the first release.

---

# 4. Examination and Syllabus Coverage

The syllabus should be represented hierarchically and remain configurable by recruitment cycle and stream.

### Expected hierarchy

```text
SEBI Grade A
│
├── Recruitment Cycle
│
├── Phase 1
│   ├── Paper 1
│   │   ├── General Awareness
│   │   ├── English Language
│   │   ├── Quantitative Aptitude
│   │   └── Reasoning Ability
│   │
│   └── Paper 2
│       └── Stream-specific subjects
│
├── Phase 2
│   ├── Paper 1
│   │   └── English Descriptive
│   │
│   └── Paper 2
│       └── Stream-specific subjects
│
└── Revision and Mock Assessments
```

The application must support the relevant examination phases, papers, streams, and subjects, including the IT stream preparation journey.

**Important:** The official SEBI notification for the applicable recruitment cycle is the source of truth for the syllabus, exam structure, question pattern, duration, marks, and negative marking.

Do not hardcode assumed examination rules. Store cycle-specific configuration and maintain source references and verification dates.

The syllabus catalogue should be complete and traceable before being presented as complete.

---

# 5. Application Modules

The planned application navigation will include:

| Module | Purpose |
|---|---|
| Dashboard | Daily missions, preparation overview, and next recommended action |
| Syllabus Explorer | Browse phases, papers, subjects, topics, and modules |
| Learning Workspace | Study detailed topic content |
| Practice Arena | Module quizzes, topic tests, subject tests, and mock tests |
| Revision Centre | Revision notes, flashcards, and scheduled revision |
| Mistake Notebook | Review incorrect and uncertain answers |
| Study Planner | Daily and weekly targets and study sessions |
| Performance Analytics | Coverage, accuracy, time, retention, and weak areas |
| English Writing Studio | Descriptive English writing and practice |
| Settings | Study goals, preferences, and application configuration |

Features should be introduced progressively. The initial release should prioritize the learning workflow and supporting progress tracking.

---

# 6. Home Dashboard

The home dashboard should be interactive, useful, and motivating enough to encourage daily application usage.

### Expected dashboard components

- Personalized greeting.
- Current preparation status.
- Today's study target.
- Daily missions and achievable tasks.
- Prominent **Continue Learning** action.
- Last active topic and module.
- Daily study streak.
- Consistency calendar.
- Overall syllabus coverage.
- Phase-wise and subject-wise progress.
- Today's study time versus target.
- Upcoming revisions.
- Weak topics and recommended next actions.
- Recent quiz performance.
- Progress and accuracy trends.
- Quick access to short practice sessions.

### Continue Learning

The most important dashboard action should be resuming the last active learning module.

The application should remember:

- Last visited topic.
- Last active module.
- Last reading position.
- Module completion status.

### Motivation

The dashboard should encourage consistency without creating unnecessary pressure.

Missed days should not erase historical progress or produce discouraging messages. Instead, the application should help the learner restart with manageable daily tasks.

---

# 7. Learning Workspace

The Learning Workspace is one of the most important parts of the application.

The design will follow a **Hybrid Layout** with two modes.

## 7.1 Workspace Mode

The default desktop layout contains three primary columns:

```text
+---------------------------------------------------------------+
|                        APPLICATION HEADER                     |
+---------------------------------------------------------------+
|                          BREADCRUMBS                          |
+------------------+---------------------------+----------------+
|                  |                           |                |
|  SYLLABUS        |      LEARNING CONTENT     | LEARNING TOOLS |
|  NAVIGATION      |                           |                |
|                  |      Module title         | Notes          |
|  Subjects        |      Explanations         | Bookmarks      |
|  Topics          |      Tables               | AI Assistant   |
|  Modules         |      Diagrams              | Revision       |
|                  |      Examples             |                |
|                  |      Questions            |                |
|                  |                           |                |
+------------------+---------------------------+----------------+
|                    PREVIOUS / NEXT NAVIGATION                  |
+---------------------------------------------------------------+
```

### Initial desktop dimensions

| Element | Target |
|---|---:|
| Header | 64 px |
| Breadcrumb area | 40 px |
| Left sidebar | 260 px |
| Right tools panel | 280 px |
| Centre content | Flexible |
| Reading content maximum width | 760 px |
| Main spacing | 24 px |

These are design targets rather than rigid constraints.

The centre column should never become excessively wide on larger screens.

## 7.2 Focus Mode

Focus Mode provides a distraction-free reading experience.

Expected behaviour:

- Hide both sidebars.
- Expand the reading area.
- Retain previous/next navigation.
- Retain reading progress.
- Keep notes and bookmarks accessible through a toolbar.
- Preserve the current reading position.
- Remember the user's preferred mode.

Switching between Workspace Mode and Focus Mode must never reset learning progress.

## 7.3 Topic Overview Screen

Purpose: Establish context before starting a topic.

Required elements:

| Element | Functionality |
|---|---|
| Topic heading | Topic name and syllabus path |
| Difficulty | Beginner / Intermediate / Advanced |
| Exam relevance | Relevance supported by syllabus or verified evidence |
| Learning objectives | What the learner will understand |
| Prerequisites | Required previous knowledge |
| Module list | All available modules |
| Time estimate | Estimated learning duration |
| MCQ availability | Available question count |
| Progress | Topic completion status |
| Resume | Continue from the last incomplete module |
| Start | Begin learning |

## 7.4 Module Learning Screen

This is the main reading interface.

### A. Header

- Topic name.
- Current module name.
- Difficulty.
- Module progress.
- Workspace/Focus mode switch.
- Bookmark shortcut.
- Notes shortcut.

### B. Left Sidebar — Syllabus Navigation

The navigation should follow a hierarchical tree structure.

Example:

```text
DATABASE CONCEPTS
│
├── Database Fundamentals
│   ├── Introduction
│   ├── DBMS Architecture
│   └── Database Models
│
├── Relational Model
│   ├── Relations
│   ├── Keys
│   └── Constraints
│
└── Normalization
    ├── Introduction
    ├── Database Anomalies
    ├── Functional Dependencies
    ├── First Normal Form
    ├── Second Normal Form
    ├── Third Normal Form
    └── BCNF
```

Each module should have a visible status:

| Status | Meaning |
|---|---|
| Grey | Not started |
| Blue | In progress |
| Green | Completed |
| Orange | Revision required |

### C. Centre — Learning Content

The content renderer should support:

- Headings.
- Paragraphs.
- Bullet lists.
- Tables.
- Code blocks.
- Mathematical equations.
- Diagrams and flowcharts.
- Important concept callouts.
- Warnings and notes.
- Worked examples.
- Embedded questions.
- Module summaries.

Content should be structured and loaded dynamically.

### D. Right Sidebar — Learning Tools

The panel should contain four tabs:

1. Tools
2. Notes
3. Bookmarks
4. AI Assistant

**Tools:**
- Reading progress.
- Estimated completion time.
- Quick revision.
- Flashcards.
- Practice this module.

**Notes:**
- Personal annotations.
- Notes linked to the current module or content block.
- Persistent storage.

**Bookmarks:**
- Saved concepts.
- Saved questions.
- Quick navigation to bookmarked content.

**AI Assistant:**
- Context-aware assistance.
- Explain the current concept.
- Provide additional examples.
- Clarify confusing concepts.
- Compare related topics.
- Generate practice questions where appropriate.

AI-generated content should be clearly distinguished from verified syllabus content.

### E. Bottom Navigation

The bottom navigation should provide:

- Previous module.
- Next module.
- Current module number.
- Progress indicator.
- Complete & Continue action.

The Complete & Continue action should save progress and offer a knowledge check before advancing.

A poor quiz score should recommend revision, not lock access to subsequent modules.

## 7.5 Module Lifecycle

The expected lifecycle is:

```text
NOT_STARTED
     |
     v
IN_PROGRESS
     |
     v
CONTENT_COMPLETED
     |
     v
KNOWLEDGE_CHECK_ATTEMPTED
     |
     v
COMPLETED
```

Additional rules:

- Closing a module preserves the reading position.
- Returning to a completed module does not reset progress.
- Revisions are recorded separately.
- All quiz attempts are preserved.
- Reattempts must never overwrite historical results.

---

# 8. Learning Content Standards

The objective is to eliminate conceptual gaps, not merely provide short notes.

Each topic should be divided into manageable learning modules.

### Recommended teaching structure

Where appropriate, each module should follow this sequence:

1. **Introduction:** Explain the concept in simple language.
2. **Purpose:** Why the concept exists and what problem it solves.
3. **Fundamentals:** Explain prerequisites and foundational concepts.
4. **Detailed explanation:** Cover mechanisms, rules, terminology, and technical details.
5. **Examples:** Provide practical examples, tables, diagrams, or code.
6. **Advanced concepts:** Explain exceptions, edge cases, and comparisons.
7. **Examination perspective:** Highlight important facts, common confusions, and relevant question patterns.
8. **Knowledge checkpoint:** Verify understanding through questions.

Depth should be appropriate to the topic.

For example:

- Programming topics should include code examples and complexity analysis where relevant.
- Database topics should include schemas, queries, relationships, and normalization examples.
- Networking topics should include protocol explanations and architecture diagrams.
- Operating systems topics should include process, memory, scheduling, and synchronization examples.

### Content quality requirements

- Explanations must be accurate and internally consistent.
- Technical terms must be explained clearly.
- Important distinctions should be highlighted.
- Examples should be practical.
- Official syllabus requirements must be distinguished from supplementary learning material.
- External claims should have appropriate references.
- Exam weightage and previous-year frequency must not be invented.
- Unverified information should be explicitly labelled.
- Correct answers must include explanations.
- Distractor explanations should be provided where useful.

Every topic should also have a concise revision sheet containing definitions, formulas, distinctions, important facts, and exam-focused takeaways.

---

# 9. Practice and Assessment Engine

Practice should be integrated into the learning experience.

There are two essential assessment levels.

## 9.1 Module-wise Knowledge Checks

Purpose: Verify understanding immediately after studying a module.

Proposed default configuration:

| Setting | Default |
|---|---|
| Questions | 5–10 |
| Duration | 5–10 minutes |
| Difficulty | Mixed |
| Negative marking | Configurable |
| Explanations | After submission |
| Retakes | Allowed |
| Progress | Automatically saved |

### User journey

1. Finish a learning module.
2. Start Knowledge Check.
3. Answer questions.
4. Submit.
5. Review results and explanations.
6. Revisit incorrect concepts.
7. Continue learning.

## 9.2 Topic-wise Assessments

Purpose: Test understanding of an entire topic after completing its modules.

This should use a dedicated examination interface rather than reusing the learning workspace.

### Required functionality

- Countdown timer.
- Question palette.
- Answer selection.
- Mark for review.
- Clear response.
- Previous and next navigation.
- Autosave answers.
- Submit confirmation.
- Automatic submission when time expires.

### Question palette states

| State | Meaning |
|---|---|
| Grey | Not visited |
| Red | Visited but unanswered |
| Green | Answered |
| Purple | Marked for review |
| Purple + Green | Answered and marked for review |

The timer must remain accurate after browser refresh or temporary connectivity loss.

Attempt start and expiry timestamps must be stored on the server.

## 9.3 Question Types

The question bank may support:

- Single-correct MCQs.
- Multiple-select practice questions.
- Assertion and reasoning.
- Match-the-following.
- Statement-based questions.
- Code-output questions.
- Numerical questions.
- Scenario-based questions.

Practice-only formats must not be represented as official examination formats unless supported by the applicable notification.

## 9.4 Assessment Results

The results page should show:

- Total score.
- Marks obtained.
- Correct answers.
- Incorrect answers.
- Unattempted questions.
- Accuracy.
- Time spent.
- Negative marking where applicable.

For each question:

- Question statement.
- Selected answer.
- Correct answer.
- Explanation.
- Why other options are incorrect, where available.
- Related module.
- Add to Mistake Notebook action.

Recommendations should be generated from actual performance.

Example:

- Revise functional dependencies.
- Practise more BCNF questions.
- Improve question-solving speed.
- Attempt another assessment after revision.

### Assessment integrity

- The server generates assessments.
- Every attempt has a unique ID.
- Start and expiry timestamps are server-authoritative.
- Answer submissions are validated.
- Final marks are calculated on the backend.
- Duplicate submissions are prevented.
- Results are retained as historical records.
- Correct answers must never be exposed before submission.

---

# 10. Revision Centre and Mistake Notebook

Revision is a first-class part of the application.

## 10.1 Revision Centre

The Revision Centre should contain four primary areas:

| Section | Contents |
|---|---|
| Revision Notes | Condensed topic summaries |
| Flashcards | Question-answer recall |
| Bookmarks | Saved concepts and questions |
| Mistake Notebook | Previously incorrect or uncertain questions |

The learner should be able to revise an entire topic without reopening every learning module.

## 10.2 Mistake Notebook

Incorrect or uncertain answers should be saved for later review.

Where possible, classify mistakes as:

- Conceptual misunderstanding.
- Knowledge gap.
- Careless error.
- Misreading the question.
- Time-management issue.
- Guess or uncertainty.

Every mistake should link back to its original question and relevant learning module.

Reattempting a question must create a new response record rather than overwrite the original attempt.

## 10.3 Revision Scheduling

Revision recommendations should consider:

- Date last studied.
- Previous revision outcomes.
- Assessment performance.
- Unresolved mistakes.
- Repeated incorrect responses.

The scheduling strategy should be transparent and configurable.

The application should not claim to measure long-term retention from insufficient data.

---

# 11. Progress and Analytics

The application must distinguish three separate metrics.

### 1. Learning Progress

How much required content has been covered?

### 2. Assessment Performance

How accurately and efficiently does the learner answer questions?

### 3. Retention

How well does the learner perform when revisiting previously studied concepts?

These metrics should never be merged into one misleading percentage.

### Suggested analytics

- Overall syllabus coverage.
- Phase-wise progress.
- Subject-wise progress.
- Topic completion.
- Module completion.
- Study time by day and subject.
- Assessment history.
- Accuracy trends.
- Marks obtained.
- Time per question.
- Weak concepts.
- Recurring mistakes.
- Revision history.
- Retention trends.

### Progress calculations

Module completion:

```text
Module Completion (%) =
    Completed Required Modules
    ---------------------------  × 100
       Total Required Modules
```

Assessment accuracy:

```text
Assessment Accuracy (%) =
        Correct Answers
    ---------------------- × 100
       Attempted Questions
```

Unattempted questions must not be counted as incorrect when calculating accuracy.

Opening a page must not count as module completion.

Topic mastery should be a separate, explainable status based on:

- Required content completed.
- Assessment performance.
- Weak concepts resolved.
- Revision performance.

Mastery thresholds should be configurable and should not be presented as a prediction of examination success.

---

# 12. Study Consistency and Motivation

Consistency is one of the central problems this application should solve.

The application should encourage regular study while supporting a realistic working-professional schedule.

### Planned features

- Configurable daily study target.
- Daily missions.
- Study-session tracking.
- Daily streaks.
- Weekly consistency calendar.
- Weekly review of planned versus completed work.
- Gentle restart flow after missed days.
- Short practice sessions for busy days.
- Progress celebrations based on meaningful learning activity.

Avoid manipulative notifications, guilt-based messaging, or gamification that rewards merely opening the application.

The system should help the learner return to studying even after a break.

---

# 13. Technical Stack

The proposed technology stack:

| Layer | Technology |
|---|---|
| Frontend | React + TypeScript + Vite |
| Styling | Tailwind CSS |
| UI Components | shadcn/ui |
| Routing | React Router |
| Server State | TanStack Query |
| Backend | Python + FastAPI |
| Validation | Pydantic |
| ORM | SQLAlchemy 2.x |
| Database | PostgreSQL |
| Migrations | Alembic |
| Charts | Recharts |
| Testing | Frontend and backend automated tests |

The stack should remain modular and maintainable.

Avoid introducing unnecessary infrastructure before a concrete requirement exists.

---

# 14. Application Architecture

Use a feature-oriented frontend architecture and a layered backend architecture.

## 14.1 Frontend Structure

```text
src/
│
├── app/
│   ├── router.tsx
│   ├── providers.tsx
│   └── queryClient.ts
│
├── components/
│   ├── ui/
│   ├── layout/
│   └── shared/
│
├── features/
│   │
│   ├── dashboard/
│   │
│   ├── syllabus/
│   │
│   ├── learning/
│   │   ├── pages/
│   │   ├── components/
│   │   ├── content-renderer/
│   │   ├── hooks/
│   │   ├── services/
│   │   └── types/
│   │
│   ├── assessment/
│   │
│   ├── revision/
│   │
│   ├── mistakes/
│   │
│   ├── planner/
│   │
│   └── analytics/
│
├── services/
│   ├── apiClient.ts
│   └── authService.ts
│
└── styles/
    ├── globals.css
    └── design-tokens.css
```

Each feature should own its components, hooks, services, and types wherever practical.

Shared components should be extracted only when they are genuinely reusable.

## 14.2 Backend Structure

```text
backend/
│
├── app/
│   ├── main.py
│   │
│   ├── core/
│   │   ├── config.py
│   │   ├── security.py
│   │   └── database.py
│   │
│   ├── api/
│   │   └── v1/
│   │
│   ├── modules/
│   │   ├── syllabus/
│   │   ├── learning/
│   │   ├── content/
│   │   ├── progress/
│   │   ├── assessment/
│   │   ├── revision/
│   │   ├── notes/
│   │   ├── bookmarks/
│   │   └── analytics/
│   │
│   ├── models/
│   ├── schemas/
│   ├── repositories/
│   └── services/
│
├── migrations/
├── tests/
└── requirements.txt
```

### Backend responsibilities

- API layer: HTTP request and response handling.
- Schema layer: Request and response validation.
- Service layer: Application business logic.
- Repository layer: Database operations.
- Model layer: SQLAlchemy entities and relationships.

Business logic should not be scattered across API endpoints.

## 14.3 Initial API Specification

These are proposed API contracts, not implemented endpoints.

| Method | Endpoint | Purpose |
|---|---|---|
| GET | `/api/v1/topics/{id}` | Get topic details |
| GET | `/api/v1/topics/{id}/modules` | Get topic modules |
| GET | `/api/v1/modules/{id}` | Get module content |
| POST | `/api/v1/modules/{id}/start` | Start learning |
| PUT | `/api/v1/modules/{id}/progress` | Update progress |
| POST | `/api/v1/modules/{id}/complete` | Complete module |
| GET | `/api/v1/modules/{id}/quiz` | Get knowledge check |
| POST | `/api/v1/assessments/start` | Start assessment |
| PUT | `/api/v1/attempts/{id}/answers` | Save answer |
| POST | `/api/v1/attempts/{id}/submit` | Submit assessment |
| GET | `/api/v1/attempts/{id}/results` | Retrieve results |
| POST | `/api/v1/bookmarks` | Create bookmark |
| POST | `/api/v1/notes` | Save note |
| GET | `/api/v1/topics/{id}/analytics` | Get topic analytics |
| GET | `/api/v1/revision/queue` | Get revision queue |

All user-specific endpoints must enforce ownership and authorization.

---

# 15. Content and Database Architecture

## 15.1 Content Hierarchy

The content system should be independent of the frontend.

```text
Exam / Recruitment Cycle
    |
    v
Phase
    |
    v
Paper
    |
    v
Subject
    |
    v
Topic
    |
    v
Module
    |
    v
Ordered Content Blocks
    |
    v
Knowledge Check
```

## 15.2 Initial Logical Entities

| Entity | Responsibility |
|---|---|
| ExamCycle | Recruitment cycle and source notification |
| Phase | Examination phase |
| Paper | Examination paper |
| Subject | Subject catalogue |
| Topic | Syllabus topic |
| Module | Learning unit |
| ContentBlock | Ordered learning content |
| Question | Question bank |
| QuestionOption | Question answer options |
| Assessment | Assessment configuration |
| AssessmentAttempt | Individual examination attempt |
| UserAnswer | User's selected answer |
| AssessmentResult | Calculated assessment result |
| UserModuleProgress | Module progress |
| UserTopicProgress | Topic progress and mastery |
| LearningSession | Study activity record |
| UserNote | Personal notes |
| Bookmark | Saved content or question |
| Flashcard | Active recall material |
| RevisionRecord | Scheduled revision history |

Use UUID primary keys, timestamps, suitable indexes, foreign-key constraints, and database migrations.

Canonical syllabus/content records must be separate from individual user progress records.

## 15.3 Example Content Object

A simplified representation:

```json
{
  "module_slug": "database-normalization",
  "title": "Database Normalization",
  "difficulty": "intermediate",
  "estimated_minutes": 45,
  "learning_objectives": [
    "Understand database anomalies",
    "Understand functional dependencies",
    "Differentiate normal forms"
  ],
  "blocks": [
    {
      "id": "normalization-intro",
      "type": "heading",
      "level": 2,
      "content": "Introduction to Normalization"
    },
    {
      "id": "normalization-definition",
      "type": "paragraph",
      "content": "Normalization is the process of..."
    },
    {
      "id": "normalization-key-idea",
      "type": "callout",
      "variant": "important",
      "title": "Key Concept",
      "content": "Normalization helps reduce redundancy."
    }
  ]
}
```

In production, content blocks should have:

- Unique IDs.
- Defined types.
- Validation schemas.
- Ordering.
- Version information.

Content must be rendered safely. Never execute arbitrary HTML or scripts from stored learning content.

## 15.4 Why Structured Content?

This architecture allows us to:

- Write learning content once.
- Render it through reusable components.
- Change the UI centrally.
- Update content without rewriting frontend pages.
- Reuse content for revision notes and AI assistance.
- Associate questions with exact learning modules.
- Maintain content versions and correction history.

---

# 16. Security and Quality Requirements

### Security

- Keep secrets in environment variables.
- Never commit credentials or API keys.
- Validate every API request.
- Enforce authorization and user ownership.
- Keep correct answers hidden during active assessments.
- Calculate examination marks on the backend.
- Enforce attempt expiry on the server.
- Prevent duplicate submissions.
- Preserve immutable assessment history.
- Use database transactions for assessment submission.
- Apply suitable rate limiting and input validation.
- Maintain database backups and migrations.

### Reliability

- Preserve reading position across navigation and refresh.
- Autosave notes and progress.
- Show visible save and error states.
- Persist assessment answers reliably.
- Handle connectivity loss and retry behaviour.
- Implement proper loading, empty, error, and success states.

### Accessibility

Target WCAG 2.2 AA.

Requirements include:

- Keyboard navigation.
- Visible focus indicators.
- Semantic controls.
- Sufficient colour contrast.
- Screen-reader-friendly components.
- Responsive desktop, tablet, and mobile layouts.

### Testing

Critical workflows must have automated tests.

- Unit tests for progress and scoring calculations.
- Tests for content validation and rendering.
- Backend API integration tests.
- Authorization tests.
- Assessment timer and expiry tests.
- Duplicate submission tests.
- Answer persistence tests.
- End-to-end tests for the main learning journey.

---

# 17. Development Roadmap

Development should be divided into small, testable milestones.

## Milestone 0 — Product and Repository Foundation

- Establish repository documentation.
- Define project conventions.
- Confirm syllabus source-of-truth.
- Finalize initial design tokens.
- Define frontend and backend architecture.
- Set up local development instructions.

## Milestone 1 — Learning Workspace UI

- Create React + TypeScript + Vite application.
- Implement design tokens.
- Build reusable UI primitives.
- Implement application shell.
- Build hybrid three-column layout.
- Implement Workspace and Focus modes.
- Build Topic Overview screen.
- Build Module Learning screen.
- Implement hierarchical module navigation.
- Implement structured content renderer.
- Use realistic sample Database Normalization content.
- Implement responsive layouts.

## Milestone 2 — Learning Persistence

- Establish FastAPI backend.
- Set up PostgreSQL.
- Implement syllabus and module APIs.
- Add content validation.
- Persist reading position.
- Persist module progress.
- Implement notes and bookmarks.

## Milestone 3 — Assessment Engine

- Implement question bank.
- Implement module knowledge checks.
- Implement topic assessments.
- Build question palette.
- Implement server-authoritative timer.
- Persist answers.
- Implement scoring and results.
- Add answer explanations.

## Milestone 4 — Revision and Analytics

- Implement Mistake Notebook.
- Implement flashcards.
- Build revision queue.
- Track learning sessions.
- Implement topic analytics.
- Implement weak-concept identification.

## Milestone 5 — Dashboard and Preparation Workflow

- Build interactive home dashboard.
- Add daily study missions.
- Implement study goals.
- Add consistency calendar.
- Integrate revision reminders.
- Add weak-topic recommendations.
- Implement broader subject and phase-level mock workflows.

## Milestone 6 — Hardening and Deployment

- Complete automated tests.
- Review security and data integrity.
- Validate syllabus and content.
- Add backup procedures.
- Configure deployment.
- Test complete desktop and mobile workflows.

---

# 18. MVP Acceptance Criteria

The first meaningful MVP should allow the learner to complete one topic from beginning to end.

### Recommended first topic: Database Normalization

This topic can exercise:

- Detailed theoretical explanations.
- Nested modules.
- Tables and comparisons.
- Technical examples.
- Knowledge-check MCQs.
- Topic-level assessments.
- Revision notes.
- Progress tracking.
- Analytics.

### Learning Workspace MVP checklist

- [ ] Responsive application shell.
- [ ] Hybrid three-column layout.
- [ ] Workspace and Focus modes.
- [ ] Reading position preservation.
- [ ] Topic overview.
- [ ] Hierarchical module navigation.
- [ ] Structured content renderer.
- [ ] Dynamic content loading.
- [ ] Module navigation.
- [ ] Module completion tracking.
- [ ] Module knowledge checks.
- [ ] Topic assessments.
- [ ] Assessment result analysis.
- [ ] Notes and bookmarks.
- [ ] Mistake Notebook.
- [ ] Revision functionality.
- [ ] Topic analytics.
- [ ] Automated tests for critical workflows.

The first UI milestone may use realistic sample data. Backend persistence and secure examination behaviour should follow in subsequent milestones.

Do not mark a feature as complete until it has actually been implemented and tested.

---

# 19. Future Scope

Once the core preparation workflow is stable, the application may be extended with:

### AI Learning Assistant

- Context-aware concept explanations.
- Follow-up questions.
- Alternative examples.
- Concept comparisons.
- Personalized revision assistance.
- Question generation with validation.

### Intelligent Study Planning

- Adaptive daily study recommendations.
- Revision scheduling.
- Weak-topic prioritization.
- Study-time recommendations.
- Weekly preparation review.

### Advanced Assessment

- Subject-level tests.
- Mixed-topic practice.
- Phase-level mock tests.
- Full examination simulations.
- Historical performance comparison.

### English Writing Studio

- Essay practice.
- Precis writing.
- Reading comprehension.
- Descriptive answer organization.
- Grammar and vocabulary exercises.
- Writing feedback and progress tracking.

### Multi-user Support

- User accounts.
- Independent study progress.
- Shared question bank.
- Study groups.
- Community discussions.
- Shared preparation resources.

These features should be considered only after the core learning and assessment workflows are reliable.

---

# Guiding Principle

> Make preparation a structured, measurable, and sustainable daily activity.

SEBI Prep OS should not merely show how much content has been opened. It should help the learner understand concepts, practise them, identify gaps, revise effectively, and maintain consistency.

**The ultimate goal is to build a learning engine that can power the complete SEBI Grade A preparation journey.**

---

## Repository Status

This repository is currently at the initial documentation stage.

This README describes the intended product, design expectations, technical direction, and development roadmap. It does not imply that the listed screens, APIs, database entities, or features are already implemented.

As implementation progresses:

- Keep this README updated when product scope or architecture changes.
- Document significant technical decisions separately in `docs/decisions/`.
- Maintain setup instructions as soon as the project skeleton is introduced.
- Keep implementation status and planned functionality clearly distinguished.