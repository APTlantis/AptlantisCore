# Blue Slate Adoption Example

This example shows the minimum documentation footprint for a project adopting Blue Slate while the standard is candidate active.

## Project Manifest Entry

```toml
[governance.visual_system]
standard = "Blue Slate"
standard_path = "D:\\.library\\aptlantis_core\\blue.slate\\README.md"
adoption_level = "candidate-active"
profile = "desktop-product"
token_source = "D:\\.library\\aptlantis_core\\blue.slate\\spec\\tokens\\BlueSlate.Tokens.json"
```

## Project README Note

The project uses Blue Slate for visual tokens, layout rhythm, component density, and design-to-implementation handoff. Any local visual departures should be recorded as project-specific profile decisions rather than edits to the standard.

## Validation

Before closeout, compare screens or mockups against `Validation-Checklist.md`, confirm the token source is still current, and record unresolved gaps in the project closeout notes.
