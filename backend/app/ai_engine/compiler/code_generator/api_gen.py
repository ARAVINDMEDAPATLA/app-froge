from app.ai_engine.schemas.api_schema import APISchema

def generate_api_code(schema: APISchema) -> str:
    """
    Generates FastAPI router logic from the APISchema.
    """
    lines = [
        "from fastapi import APIRouter, Depends, HTTPException",
        "from typing import List, Dict, Any",
        "",
        "router = APIRouter()",
        ""
    ]
    
    # Define a stubbed dependency for auth if needed
    lines.append("def get_current_user():")
    lines.append("    # Stubbed auth dependency")
    lines.append("    return {'id': 1, 'role': 'user'}")
    lines.append("")

    for route in schema.routes:
        # Determine the python method name (e.g. GET /users -> get_users)
        method_lower = route.method.lower()
        # Clean path for function name e.g., /users/{id} -> users_id
        path_clean = route.path.strip('/').replace('/', '_').replace('{', '').replace('}', '')
        func_name = f"{method_lower}_{path_clean}" if path_clean else f"{method_lower}_root"
        
        # Determine route decorator
        deps = ", dependencies=[Depends(get_current_user)]" if route.requires_auth else ""
        lines.append(f"@router.{method_lower}('{route.path}'{deps})")
        
        # Determine function arguments based on path variables
        args = []
        if '{id}' in route.path:
            args.append("id: int")
        if method_lower in ['post', 'put']:
            args.append("payload: Dict[str, Any]")
            
        args_str = ", ".join(args)
        lines.append(f"async def {func_name}({args_str}):")
        lines.append(f'    """ {route.description} """')
        lines.append(f'    return {{"message": "Action {route.method} on {route.path} executed."}}')
        lines.append("")
        
    return "\n".join(lines)
