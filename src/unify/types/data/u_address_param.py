# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo
from .u_country_param import UCountryParam

__all__ = ["UAddressParam"]


class UAddressParam(TypedDict, total=False):
    """Composite object representing a physical address."""

    administrative_area: Annotated[str, PropertyInfo(alias="administrativeArea")]
    """State, province, region, or territory."""

    country: UCountryParam
    """Composite object representing a country."""

    dependent_locality: Annotated[str, PropertyInfo(alias="dependentLocality")]
    """Neighborhood, borough, district, or city sector."""

    locality: str
    """City, town, or village."""

    postal_code: Annotated[str, PropertyInfo(alias="postalCode")]
    """Postal code or ZIP code."""

    premise: str
    """Street number or building name."""

    sub_administrative_area: Annotated[str, PropertyInfo(alias="subAdministrativeArea")]
    """County or other secondary governmental division of an administrative area."""

    sub_premise: Annotated[str, PropertyInfo(alias="subPremise")]
    """Apartment, suite, office number, or other secondary unit designator."""

    thoroughfare: str
    """Street name with elements such as street type or direction."""
