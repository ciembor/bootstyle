from string import Template

# dictionary with default Bootstrap colors
default = {
                  
  "scaffolding" : {
    "@bodyBackground" : "@white",
    "@textColor" : "@grayDark",
    "@linkColor" : "#0088cc",
    "@linkColorHover" : "darken(@linkColor, 15%)"
  },
  
  "tables" : {
    "@tableBackground" : "transparent",
    "@tableBackgroundAccent" : "#f9f9f9",
    "@tableBackgroundHover" : "#f5f5f5",
    "@tableBorder" : "#dddddd"
  },
  
  "grayscale" : {
    "@black" : "#000000",
    "@grayDarker" : "#222222",
    "@grayDark" : "#333333",
    "@gray" : "#555555",
    "@grayLight" : "#999999",
    "@grayLighter" : "#eeeeee",
    "@white" : "#ffffff"
  },
  
  "accent" : {
    "@blue" : "#049cdb",
    "@green" : "#46a546",
    "@red" : "#9d261d",
    "@yellow" : "#ffc40d",
    "@orange" : "#f89406",
    "@pink" : "#c3325f",
    "@purple" : "#7a43b6"
  },

  "buttons" : {
    "@btnBackground" : "@white",
    "@btnBackgroundHighlight" : "darken(@white, 10%)",
    "@btnBorder" : "darken(@white, 20%)",
    "@btnPrimaryBackground" : "@linkColor",
    "@btnPrimaryBackgroundHighlight" : "spin(@btnPrimaryBackground, 15%)",
    "@btnInfoBackground" : "#5bc0de",
    "@btnInfoBackgroundHighlight" : "#2f96b4",
    "@btnSuccessBackground" : "#62c462",
    "@btnSuccessBackgroundHighlight" : "#51a351",
    "@btnWarningBackground" : "lighten(@orange, 15%)",
    "@btnWarningBackgroundHighlight" : "@orange",
    "@btnDangerBackground" : "#ee5f5b",
    "@btnDangerBackgroundHighlight" : "#bd362f",
    "@btnInverseBackground" : "@gray",
    "@btnInverseBackgroundHighlight" : "@grayDarker"
  },
  
  "forms" : {
    "@placeholderText" : "@grayLight",
    "@inputBackground" : "@white",
    "@inputBorder" : "#cccccc",
    "@inputDisabledBackground" : "@grayLighter",
    "@formActionsBackground" : "#f5f5f5"
  },
  
  "alerts" : {
    "@warningText" : "#c09853",
    "@warningBackground" : "#f3edd2",
    "@warningBorder" : "darken(spin(@warningBackground, -10), 3%)",
    "@errorText" : "#b94a48",
    "@errorBackground" : "#f2dede",
    "@errorBorder" : "darken(spin(@errorBackground, -10), 3%)",
    "@successText" : "#468847",
    "@successBackground" : "#dff0d8",
    "@successBorder" : "darken(spin(@successBackground, -10), 5%)",
    "@infoText" : "#3a87ad",
    "@infoBackground" : "#d9edf7",
    "@infoBorder" : "darken(spin(@infoBackground, -10), 7%)",
  },

  "navbar" : {
    "@navbarBackground" : "@grayDarker",
    "@navbarBackgroundHighlight" : "@grayDark",
    "@navbarText" : "@grayLight",
    "@navbarLinkColor" : "@grayLight",
    "@navbarLinkColorHover" : "@white",
    "@navbarLinkBackgroundHover" : "transparent",
    "@navbarLinkBackgroundActive" : "@navbarBackground",
    "@navbarSearchBackground" : "lighten(@navbarBackground, 25%)",
    "@navbarSearchBackgroundFocus" : "@white",
    "@navbarSearchBorder" : "darken(@navbarSearchBackground, 30%)",
    "@navbarSearchPlaceholderColor" : "darken(@white, 20%)",
    "@navbarBrandColor" : "@navbarLinkColor",
    "@navbarLinkColorActive" : "@navbarLinkColorHover"
  },
  
  "dropdowns" : {
    "@dropdownBackground" : "@white",
    "@dropdownBorder" : "rgba(0,0,0,.2)",
    "@dropdownLinkColor" : "@grayDark",
    "@dropdownLinkColorHover" : "@white",
    "@dropdownLinkBackgroundHover" : "@linkColor",
    "@dropdownDividerTop" : "#e5e5e5",
    "@dropdownDividerBottom" : "@white"
  },
  
  "herounit" : {
    "@heroUnitBackground" : "@grayLighter",
    "@heroUnitHeadingColor" : "inherit",
    "@heroUnitLeadColor" : "inherit"
  }
}

# template of file with LESS requires (in bootstrap called bootstrap.less)
requiresTemplate = Template("""
  // CSS Reset
  @import "${bootstrap_path}/less/reset.less";
  
  // Core variables and mixins
  @import "variables.less"; // This file should be in the same directory, it's generated with bootstyle
  @import "${bootstrap_path}/less/mixins.less";
  
  // Grid system and page structure
  @import "${bootstrap_path}/less/scaffolding.less";
  @import "${bootstrap_path}/less/grid.less";
  @import "${bootstrap_path}/less/layouts.less";
  
  // Base CSS
  @import "${bootstrap_path}/less/type.less";
  @import "${bootstrap_path}/less/code.less";
  @import "${bootstrap_path}/less/forms.less";
  @import "${bootstrap_path}/less/tables.less";
  
  // Components: common
  @import "${bootstrap_path}/less/sprites.less";
  @import "${bootstrap_path}/less/dropdowns.less";
  @import "${bootstrap_path}/less/wells.less";
  @import "${bootstrap_path}/less/component-animations.less";
  @import "${bootstrap_path}/less/close.less";
  
  // Components: Buttons & Alerts
  @import "${bootstrap_path}/less/buttons.less";
  @import "${bootstrap_path}/less/button-groups.less";
  @import "${bootstrap_path}/less/alerts.less"; // Note: alerts share common CSS with buttons and thus have styles in buttons.less
  
  // Components: Nav
  @import "${bootstrap_path}/less/navs.less";
  @import "${bootstrap_path}/less/navbar.less";
  @import "${bootstrap_path}/less/breadcrumbs.less";
  @import "${bootstrap_path}/less/pagination.less";
  @import "${bootstrap_path}/less/pager.less";
  
  // Components: Popovers
  @import "${bootstrap_path}/less/modals.less";
  @import "${bootstrap_path}/less/tooltip.less";
  @import "${bootstrap_path}/less/popovers.less";
  
  // Components: Misc
  @import "${bootstrap_path}/less/thumbnails.less";
  @import "${bootstrap_path}/less/labels-badges.less";
  @import "${bootstrap_path}/less/progress-bars.less";
  @import "${bootstrap_path}/less/accordion.less";
  @import "${bootstrap_path}/less/carousel.less";
  @import "${bootstrap_path}/less/hero-unit.less";
  
  // Utility classes
  @import "${bootstrap_path}/less/utilities.less"; // Has to be last to override when necessary
  
""")

# template of variables.less
variablesTemplate = Template("""
  // Variables.less
  // Variables to customize the look and feel of Bootstrap
  // -----------------------------------------------------
  
  
  
  // GLOBAL VALUES
  // --------------------------------------------------
  
  
  // Grays
  // -------------------------

  $grayscale

  // Accent colors
  // -------------------------

  $accent

  // Scaffolding and Links
  // -------------------------

  $scaffolding

  // Typography
  // -------------------------
  @sansFontFamily:        "Helvetica Neue", Helvetica, Arial, sans-serif;
  @serifFontFamily:       Georgia, "Times New Roman", Times, serif;
  @monoFontFamily:        Menlo, Monaco, Consolas, "Courier New", monospace;
  
  @baseFontSize:          13px;
  @baseFontFamily:        @sansFontFamily;
  @baseLineHeight:        18px;
  @altFontFamily:         @serifFontFamily;
  
  @headingsFontFamily:    inherit; // empty to use BS default, @baseFontFamily
  @headingsFontWeight:    bold;    // instead of browser default, bold
  @headingsColor:         inherit; // empty to use BS default, @textColor
  
  
  // Tables
  // -------------------------

  $tables

  // Buttons
  // -------------------------

  $buttons

  // Forms
  // -------------------------
  @inputBorderRadius:             3px;
  
  $forms
  
  // Dropdowns
  // -------------------------

  $dropdowns

  // COMPONENT VARIABLES
  // --------------------------------------------------
  
  // Z-index master list
  // -------------------------
  // Used for a bird's eye view of components dependent on the z-axis
  // Try to avoid customizing these :)
  @zindexDropdown:          1000;
  @zindexPopover:           1010;
  @zindexTooltip:           1020;
  @zindexFixedNavbar:       1030;
  @zindexModalBackdrop:     1040;
  @zindexModal:             1050;
  
  
  // Sprite icons path
  // -------------------------
  @iconSpritePath:          "../img/glyphicons-halflings.png";
  @iconWhiteSpritePath:     "../img/glyphicons-halflings-white.png";
  
  // Hr border color
  // -------------------------
  @hrBorder:                @grayLighter;
  
  // Navbar
  // -------------------------
  @navbarHeight:                    40px;

  $navbar

  // Hero unit
  // -------------------------

  $herounit

  // Form states and alerts
  // -------------------------

  $alerts

  // GRID
  // --------------------------------------------------
  
  // Default 940px grid
  // -------------------------
  @gridColumns:             12;
  @gridColumnWidth:         60px;
  @gridGutterWidth:         20px;
  @gridRowWidth:            (@gridColumns * @gridColumnWidth) + (@gridGutterWidth * (@gridColumns - 1));
  
  // Fluid grid
  // -------------------------
  @fluidGridColumnWidth:    6.382978723%;
  @fluidGridGutterWidth:    2.127659574%;

""")