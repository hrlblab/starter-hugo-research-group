---
# A Demo section created with the Blank widget.
# Any elements can be added in the body: https://wowchemy.com/docs/writing-markdown-latex/
# Add more sections by duplicating this file and customizing to your requirements.

widget: blank  # See https://wowchemy.com/docs/page-builder/
headless: true  # This file represents a page section.
weight: 70  # Order that this section will appear.

title: "Alumni"
subtitle: ""

design:
  # Choose how many columns the section has. Valid values: 1 or 2.
  columns: '1'
  background:
    # Apply a background color, gradient, or image.
    #   Uncomment (by removing `#`) an option to apply it.
    #   Choose a light or dark text color by setting `text_color_light`.
    #   Any HTML color name or Hex value is valid.
    color: White
    #gradient_start: Turquoise
    #gradient_end: PaleTurquoise
    text_color_light: False
    image_darken: 0

#{{< gdocs src="https://docs.google.com/spreadsheets/d/1M0Pfjb8c0xg1_VpBaszsbolFus1YTSiT/edit?usp=sharing&ouid=115028073207757661230&rtpof=true&sd=true" >}}
---
{{< table src="results.csv" header=true caption=""  delimiter="," >}}
