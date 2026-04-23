# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel
from .u_country import UCountry

__all__ = ["UAddress"]


class UAddress(BaseModel):
    """Composite object representing a physical address."""

    administrative_area: Optional[str] = None
    """State, province, region, or territory."""

    country: Optional[UCountry] = None
    """Composite object representing a country."""

    dependent_locality: Optional[str] = None
    """Neighborhood, borough, district, or city sector."""

    locality: Optional[str] = None
    """City, town, or village."""

    postal_code: Optional[str] = None
    """Postal code or ZIP code."""

    premise: Optional[str] = None
    """Street number or building name."""

    sub_administrative_area: Optional[str] = None
    """County or other secondary governmental division of an administrative area."""

    sub_premise: Optional[str] = None
    """Apartment, suite, office number, or other secondary unit designator."""

    thoroughfare: Optional[str] = None
    """Street name with elements such as street type or direction."""
