# 🤝 Contributing to Recipe Hub

Thank you for your interest in contributing to **Recipe Hub**!  
Whether you want to fix bugs, add new features, improve documentation, or enhance the UI, this guide will help you get started quickly and contribute effectively.  

By following these guidelines, you’ll help us maintain code quality, ensure smooth collaboration, and make the project more enjoyable for everyone.

---

## 📋 Table of Contents

- [🍽️ Prerequisites](#prerequisites) – Tools and software you’ll need before starting.  
- [📂 Project Structure](#project-structure) – Overview of folders and files to help you navigate the codebase.  
- [⚙️ Setup Instructions](#setup-instructions) – How to set up the project locally.  
- [🏃 Running the Application](#running-the-application) – Start the app and verify everything works.  
- [🛠️ Development Workflow](#development-workflow) – Branching, commits, and PR guidelines.  
- [🎨 Code Style Guidelines](#code-style-guidelines) – Coding conventions for frontend and backend.  
- [🧪 Testing](#testing) – Running and writing tests to ensure quality.  
- [📤 Submitting Changes](#submitting-changes) – Creating pull requests and following the review process.  
- [🐞 Troubleshooting](#troubleshooting) – Common issues and solutions during setup or development.

> 💡 **Tip:** Use this guide as your roadmap for contributing efficiently and effectively.

## 🔧 Prerequisites

Before you start contributing, make sure you have the following installed on your machine:

- **Node.js** (v16 or higher) – Required to run the frontend and install dependencies.  
  [Download Node.js](https://nodejs.org/)

- **Python** (v3.8 or higher) – Needed for backend scripts, automation, or testing.  
  [Download Python](https://python.org/)

- **Git** – To clone repositories, manage branches, and submit contributions.  
  [Download Git](https://git-scm.com/)

- **Docker** *(optional but recommended)* – For containerized development and consistent environment setup.  
  [Download Docker](https://docker.com/)

> 💡 **Tip:** Verify installations by running `node -v`, `python --version`, and `git --version` in your terminal. This ensures all tools are correctly set up before proceeding.

## 📁 Project Structure

```
Recipe-Hub/
├── apps/
│   ├── servers/          # FastAPI Backend
│   │   ├── app/
│   │   │   ├── api/      # API endpoints
│   │   │   ├── core/     # Configuration
│   │   │   ├── models/   # Database models
│   │   │   ├── schemas/  # Pydantic schemas
│   │   │   └── services/ # Business logic
│   │   ├── requirements.txt
│   │   └── venv/         # Python virtual environment
│   └── web/              # React Frontend
│       ├── src/
│       │   ├── components/ # React components
│       │   ├── pages/      # Page components
│       │   ├── lib/        # API and utilities
│       │   └── hooks/      # Custom hooks
│       ├── package.json
│       └── node_modules/
├── data/                 # Sample data and media
├── docker/              # Docker configurations
└── scripts/             # Development scripts
```

## 🚀 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/Recipe-Hub.git
cd Recipe-Hub
```

### 2. Backend Setup (FastAPI)

```bash
# Navigate to backend directory
cd apps/servers

# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\Activate.ps1
# On macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Start the backend server
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

The backend will be available at:
- **API**: `http://localhost:8000`
- **API Documentation**: `http://localhost:8000/api/docs`
- **Health Check**: `http://localhost:8000/api/v1/health`

### 3. Frontend Setup (React)

Open a new terminal and run:

```bash
# Navigate to frontend directory
cd apps/web

# Install dependencies
npm install

# Start the development server
npm run dev
```

The frontend will be available at `http://localhost:5173` (or the next available port).

## 🏃‍♂️ Running the Application

### Option 1: Manual Setup (Recommended for Development)

1. **Start Backend** (Terminal 1):
   ```bash
   cd apps/servers
   venv\Scripts\Activate.ps1  # Windows
   uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
   ```

2. **Start Frontend** (Terminal 2):
   ```bash
   cd apps/web
   npm run dev
   ```

### Option 2: Docker Setup

```bash
# From project root
docker-compose up --build
```

### Option 3: Development Script

```bash
# Make script executable (Linux/macOS)
chmod +x scripts/dev.sh

# Run development script
./scripts/dev.sh
```

## 🔄 Development Workflow

### 1. Create a Feature Branch

```bash
git checkout -b feature/your-feature-name
```

### 2. Make Your Changes

- **Backend**: Add new endpoints in `apps/servers/app/api/v1/`
- **Frontend**: Add new components in `apps/web/src/components/`
- **Database**: Update models in `apps/servers/app/models/`

### 3. Test Your Changes

```bash
# Backend tests
cd apps/servers
python -m pytest

# Frontend tests
cd apps/web
npm test
```

### 4. Commit Your Changes

```bash
git add .
git commit -m "feat: add new recipe search functionality"
```

### 5. Push and Create Pull Request

```bash
git push origin feature/your-feature-name
```

Then create a Pull Request on GitHub.

## 📝 Code Style Guidelines

### Backend (Python/FastAPI)

- Follow **PEP 8** style guidelines
- Use **type hints** for all function parameters and return values
- Write **docstrings** for all functions and classes
- Use **async/await** for database operations

```python
async def get_recipe(recipe_id: int) -> Recipe:
    """
    Retrieve a recipe by its ID.
    
    Args:
        recipe_id: The unique identifier of the recipe
        
    Returns:
        Recipe object if found
        
    Raises:
        HTTPException: If recipe is not found
    """
    # Implementation here
```

### Frontend (React/TypeScript)

- Use **functional components** with hooks
- Define **TypeScript interfaces** for all props and data
- Use **Tailwind CSS** for styling
- Follow **React best practices**

```typescript
interface RecipeCardProps {
  recipe: Recipe;
  onEdit?: (recipe: Recipe) => void;
}

const RecipeCard: React.FC<RecipeCardProps> = ({ recipe, onEdit }) => {
  // Component implementation
};
```

## 🧪 Testing

### Backend Testing

```bash
cd apps/servers
python -m pytest tests/ -v
```

### Frontend Testing

```bash
cd apps/web
npm test
```

### Manual Testing

1. **API Testing**: Use the interactive docs at `http://localhost:8000/api/docs`
2. **Frontend Testing**: Test all user flows in the browser
3. **Integration Testing**: Ensure frontend and backend work together

## 📤 Submitting Changes

### 1. Fork the Repository

Click the "Fork" button on GitHub and clone your fork.

### 2. Create a Pull Request

1. Push your changes to your fork
2. Create a Pull Request with:
   - Clear title describing the change
   - Detailed description of what was changed
   - Screenshots (for UI changes)
   - Reference to any related issues

### 3. Pull Request Template

```markdown
## Description
Brief description of changes

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Breaking change
- [ ] Documentation update

## Testing
- [ ] Backend tests pass
- [ ] Frontend tests pass
- [ ] Manual testing completed

## Screenshots (if applicable)
Add screenshots here

## Checklist
- [ ] Code follows style guidelines
- [ ] Self-review completed
- [ ] Documentation updated
```

## 🐛 Troubleshooting

### Common Issues

#### Backend Issues

**Problem**: `ModuleNotFoundError: No module named 'app'`
```bash
# Solution: Make sure you're in the correct directory
cd apps/servers
venv\Scripts\Activate.ps1
uvicorn app.main:app --reload
```

**Problem**: `ImportError: cannot import name 'settings'`
```bash
# Solution: Install missing dependencies
pip install pydantic-settings email-validator
```

#### Frontend Issues

**Problem**: `404 Not Found` on frontend
```bash
# Solution: Check if Vite is running and note the correct port
npm run dev
# Look for the "Local:" URL in the output
```

**Problem**: No styling (Tailwind not working)
```bash
# Solution: Reinstall dependencies and restart
rm -rf node_modules package-lock.json
npm install
npm run dev
```

#### Port Conflicts

**Problem**: Port already in use
```bash
# Solution: Kill processes using the port or use different ports
# Windows:
netstat -ano | findstr :8000
taskkill /PID <PID> /F

# Or change ports in the commands:
uvicorn app.main:app --reload --port 8001
npm run dev -- --port 3000
```

### 🆘 Getting Help

If you run into issues or have questions while contributing, here’s where to get support:

- **GitHub Issues** – Report bugs or request new features.  
- **GitHub Discussions** – Ask questions, share ideas, or discuss improvements.  
- **Discord** – Join our community server to chat with maintainers and other contributors.  
- **Documentation** – Check the API docs at `/api/docs` for backend endpoints and usage.  

> 💡 **Tip:** Always search existing issues and discussions before creating a new one to avoid duplicates.

---

## 🎯 Areas for Contribution

### 🌱 Good First Issues
These tasks are perfect for newcomers looking to get started:

- [ ] Add recipe categories  
- [ ] Implement user authentication  
- [ ] Add recipe rating system  
- [ ] Create recipe search filters  
- [ ] Add recipe image upload  
- [ ] Implement user profiles  
- [ ] Add recipe comments  
- [ ] Create recipe collections  

> 🚀 **Tip:** Pick an issue, comment that you’re working on it, and start contributing! It’s a great way to learn the codebase and get comfortable with the project workflow.


### 🚀 Advanced Features (Planned / Future)

These are some exciting features we plan to implement in Recipe Hub. Contributions are welcome!

- [ ] Recipe recommendation system  
- [ ] Social features (following other users)  
- [ ] Recipe sharing functionality  
- [ ] Mobile app support  
- [ ] Import recipes from other websites  
- [ ] Display nutritional information  
- [ ] Meal planning and weekly menus  

---

## 📚 Additional Resources

Here are some official resources to help you work on Recipe Hub efficiently:

- [FastAPI Documentation](https://fastapi.tiangolo.com/) – Backend framework reference  
- [React Documentation](https://react.dev/) – Frontend framework reference  
- [Tailwind CSS Documentation](https://tailwindcss.com/) – Styling and responsive design  
- [TypeScript Documentation](https://www.typescriptlang.org/) – Strongly-typed JavaScript guidance  

---

## 🙏 Thank You

Thank you for contributing to **Recipe Hub**!  

Your time, ideas, and code help make this project better for everyone. If you have any questions or need guidance:  

- Reach out to the maintainers via GitHub issues or PR comments  
- Join the community discussions  

Happy coding, and may your recipes always be delicious! 🍲✨

