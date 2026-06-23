from app.ai_engine.schemas.ui_schema import UISchema

def generate_ui_code(schema: UISchema) -> str:
    """
    Generates React components (TSX) from the UISchema.
    Returns a consolidated string for simplicity in the demo.
    """
    lines = [
        "import React from 'react';",
        "import { BrowserRouter as Router, Route, Routes, Link } from 'react-router-dom';",
        ""
    ]

    # Generate Component stubs
    components_created = set()
    for page in schema.pages:
        for comp in page.components:
            if comp.name not in components_created:
                lines.append(f"export const {comp.name} = () => {{")
                lines.append(f"  return (")
                lines.append(f"    <div className='p-4 border rounded shadow-sm my-2'>")
                lines.append(f"      <h3 className='font-bold'>{comp.name}</h3>")
                lines.append(f"      <p className='text-sm text-gray-500'>{comp.description}</p>")
                lines.append(f"      {{/* Placeholder for {comp.type} component */}}")
                lines.append(f"    </div>")
                lines.append(f"  );")
                lines.append(f"}};\n")
                components_created.add(comp.name)
                
    # Generate Page stubs
    for page in schema.pages:
        lines.append(f"export const {page.name}Page = () => {{")
        lines.append(f"  return (")
        lines.append(f"    <div className='p-8'>")
        lines.append(f"      <h1 className='text-2xl font-bold mb-4'>{page.name}</h1>")
        for comp in page.components:
            lines.append(f"      <{comp.name} />")
        lines.append(f"    </div>")
        lines.append(f"  );")
        lines.append(f"}};\n")

    # Generate App Router
    lines.append("export const AppRouter = () => {")
    lines.append("  return (")
    lines.append("    <Router>")
    lines.append("      <nav className='p-4 bg-gray-100 flex gap-4'>")
    for page in schema.pages:
        lines.append(f"        <Link to='{page.route}' className='text-blue-500 hover:underline'>{page.name}</Link>")
    lines.append("      </nav>")
    lines.append("      <Routes>")
    for page in schema.pages:
        lines.append(f"        <Route path='{page.route}' element={{<{page.name}Page />}} />")
    lines.append("      </Routes>")
    lines.append("    </Router>")
    lines.append("  );")
    lines.append("};\n")

    return "\n".join(lines)
