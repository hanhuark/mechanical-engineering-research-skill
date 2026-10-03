Add-Type -AssemblyName System.Drawing

$scriptRoot = Split-Path -Parent $MyInvocation.MyCommand.Path
$outputPath = Join-Path $scriptRoot 'mechanical-engineering-research-skill-social-preview.png'
$canvas = New-Object System.Drawing.Bitmap 1280, 640
$graphics = [System.Drawing.Graphics]::FromImage($canvas)

try {
    $graphics.SmoothingMode = [System.Drawing.Drawing2D.SmoothingMode]::AntiAlias
    $graphics.InterpolationMode = [System.Drawing.Drawing2D.InterpolationMode]::HighQualityBicubic
    $graphics.TextRenderingHint = [System.Drawing.Text.TextRenderingHint]::AntiAliasGridFit
    $graphics.Clear([System.Drawing.Color]::FromArgb(8, 25, 33))

    $teal = [System.Drawing.Color]::FromArgb(15, 118, 110)
    $cyan = [System.Drawing.Color]::FromArgb(103, 232, 249)
    $orange = [System.Drawing.Color]::FromArgb(249, 115, 22)
    $cream = [System.Drawing.Color]::FromArgb(244, 246, 238)
    $muted = [System.Drawing.Color]::FromArgb(170, 192, 195)
    $panel = [System.Drawing.Color]::FromArgb(17, 48, 59)
    $line = New-Object System.Drawing.Pen ([System.Drawing.Color]::FromArgb(74, 124, 133)), 2
    $cyanPen = New-Object System.Drawing.Pen $cyan, 10
    $orangePen = New-Object System.Drawing.Pen $orange, 10
    $whiteBrush = New-Object System.Drawing.SolidBrush $cream
    $mutedBrush = New-Object System.Drawing.SolidBrush $muted
    $tealBrush = New-Object System.Drawing.SolidBrush $teal
    $panelBrush = New-Object System.Drawing.SolidBrush $panel
    $titleFont = New-Object System.Drawing.Font 'Aptos Display', 33, ([System.Drawing.FontStyle]::Bold)
    $subtitleFont = New-Object System.Drawing.Font 'Aptos', 14, ([System.Drawing.FontStyle]::Regular)
    $labelFont = New-Object System.Drawing.Font 'Aptos', 13, ([System.Drawing.FontStyle]::Bold)
    $smallFont = New-Object System.Drawing.Font 'Aptos', 11, ([System.Drawing.FontStyle]::Regular)

    $graphics.FillRectangle($tealBrush, 54, 55, 8, 103)
    $graphics.DrawString('MECHANICAL ENGINEERING', $titleFont, $whiteBrush, 82, 48)
    $graphics.DrawString('RESEARCH SKILL', $titleFont, $whiteBrush, 82, 89)
    $graphics.DrawString('THERMAL FLUIDS  |  TECHNICAL WRITING  |  DATA ANALYSIS  |  MENTORING', $subtitleFont, $mutedBrush, 84, 143)
    $graphics.DrawLine($line, 54, 184, 1226, 184)

    $panels = @(
        (New-Object System.Drawing.Rectangle 54, 220, 348, 320),
        (New-Object System.Drawing.Rectangle 466, 220, 348, 320),
        (New-Object System.Drawing.Rectangle 878, 220, 348, 320)
    )
    foreach ($currentPanel in $panels) {
        $graphics.FillRectangle($panelBrush, $currentPanel)
        $graphics.DrawRectangle($line, $currentPanel)
    }

    # Illustrative heat and flow panel.
    $graphics.FillRectangle($tealBrush, 92, 270, 20, 190)
    $graphics.DrawLine($orangePen, 150, 305, 330, 305)
    $graphics.DrawLine($orangePen, 150, 365, 330, 365)
    $graphics.DrawLine($cyanPen, 150, 425, 330, 425)
    $graphics.FillEllipse((New-Object System.Drawing.SolidBrush $orange), 118, 275, 26, 26)
    $graphics.FillEllipse((New-Object System.Drawing.SolidBrush $orange), 118, 335, 26, 26)
    $graphics.FillEllipse((New-Object System.Drawing.SolidBrush $cyan), 118, 395, 26, 26)
    $graphics.DrawString('PHYSICS', $labelFont, $whiteBrush, 78, 490)
    $graphics.DrawString('assumptions, regimes, limits', $smallFont, $mutedBrush, 78, 512)

    # Illustrative evidence panel.
    $paper = New-Object System.Drawing.Rectangle 552, 264, 170, 215
    $graphics.FillRectangle((New-Object System.Drawing.SolidBrush ([System.Drawing.Color]::FromArgb(232, 248, 247))), $paper)
    $graphics.DrawRectangle($line, $paper)
    for ($row = 0; $row -lt 5; $row++) {
        $y = 298 + ($row * 28)
        $graphics.DrawLine((New-Object System.Drawing.Pen ([System.Drawing.Color]::FromArgb(45, 96, 100)), 3), 578, $y, 694, $y)
    }
    $graphics.FillEllipse((New-Object System.Drawing.SolidBrush $orange), 668, 392, 28, 28)
    $graphics.DrawString('EVIDENCE', $labelFont, $whiteBrush, 490, 490)
    $graphics.DrawString('sources, claims, conclusions', $smallFont, $mutedBrush, 490, 512)

    # Illustrative workflow panel.
    $nodeBrush = New-Object System.Drawing.SolidBrush $cyan
    $nodes = @(@(958, 286), @(1078, 350), @(958, 414))
    $graphics.DrawLine($line, 978, 306, 1058, 340)
    $graphics.DrawLine($line, 1058, 360, 978, 404)
    foreach ($node in $nodes) { $graphics.FillEllipse($nodeBrush, $node[0], $node[1], 40, 40) }
    $graphics.DrawString('WORKFLOW', $labelFont, $whiteBrush, 902, 490)
    $graphics.DrawString('plan, check, revise', $smallFont, $mutedBrush, 902, 512)

    $graphics.DrawString('OPEN SOURCE  |  CODEX AND CLAUDE CODE', $subtitleFont, $mutedBrush, 54, 580)
    $canvas.Save($outputPath, [System.Drawing.Imaging.ImageFormat]::Png)
}
finally {
    foreach ($item in @($titleFont, $subtitleFont, $labelFont, $smallFont, $line, $cyanPen, $orangePen, $whiteBrush, $mutedBrush, $tealBrush, $panelBrush, $nodeBrush, $graphics, $canvas)) {
        if ($null -ne $item) { $item.Dispose() }
    }
}
