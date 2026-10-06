from .core import Hazard


def validate_transition(item: Hazard, target: str) -> None:
    allowed = {"draft": {"active", "closed"}, "active": {"closed"}, "closed": set()}
    if target not in allowed[item.status]:
        raise ValueError(f"不允许从 {item.status} 转为 {target}")

