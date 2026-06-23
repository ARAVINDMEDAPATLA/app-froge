from app.ai_engine.schemas.db_schema import DBSchema

def generate_db_code(schema: DBSchema) -> str:
    """
    Generates SQLAlchemy models from the DBSchema.
    """
    lines = [
        "from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Float",
        "from sqlalchemy.orm import declarative_base, relationship",
        "",
        "Base = declarative_base()",
        ""
    ]
    
    # Map abstract schema types to SQLAlchemy types
    type_map = {
        "int": "Integer",
        "integer": "Integer",
        "varchar": "String",
        "string": "String",
        "boolean": "Boolean",
        "decimal": "Float",
        "float": "Float"
    }

    for table in schema.tables:
        lines.append(f"class {table.name}(Base):")
        lines.append(f"    __tablename__ = '{table.name.lower()}s'")
        
        for col in table.columns:
            col_type = type_map.get(col.type.lower(), "String")
            args = [col_type]
            
            if col.is_primary_key:
                args.append("primary_key=True")
                args.append("index=True")
            if col.is_foreign_key and col.references:
                # E.g., ForeignKey('users.id')
                # Parse references string which might be "User.id" -> "users.id"
                ref_table, ref_col = col.references.split('.')
                args.append(f"ForeignKey('{ref_table.lower()}s.{ref_col}')")
                
            args_str = ", ".join(args)
            lines.append(f"    {col.name} = Column({args_str})")
            
        lines.append("")
        
    return "\n".join(lines)
