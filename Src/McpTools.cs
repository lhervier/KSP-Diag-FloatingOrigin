using System;
using System.Collections.Generic;
using UnityEngine;
using com.github.lhervier.ksp.mcpserver;

namespace com.github.lhervier.ksp.diag.floatingorigin
{
    /// <summary>
    /// What KSP-MCPServer, when it is installed, offers of this mod as tools: its buttons, the reading of
    /// its table, and the moving of its window. Each method works on the window loaded in the scene.
    /// Nothing here is needed to play by hand, and this mod runs the same without KSP-MCPServer: only
    /// that server reads the attribute.
    /// </summary>
    internal static class McpTools
    {
        [McpTool("floatingorigin_record",
            "Presses Record in the window of KSP Diag - Floating Origin: freezes the line in progress into " +
                "its table and returns it (UniversalTime, RotatingFrame, DirectRotAngle, InverseRotAngle, " +
                "SphereOrigin, OriginDistance, Shifts since the line before, LastShift); null when there is no " +
                "body to read.")]
        internal static object Record()
        {
            return Window().Record();
        }

        [McpTool("floatingorigin_read",
            "Reads the window of KSP Diag - Floating Origin: its recorded lines and the line in " +
                "progress.")]
        internal static object Read()
        {
            KSPDiagFloatingOrigin window = Window();
            return new Dictionary<string, object>
            {
                { "lines", new List<Reading>(window.Lines) },
                { "live", window.Live }
            };
        }

        [McpTool("floatingorigin_clear", "Presses Clear table in the window of KSP Diag - Floating Origin.")]
        internal static void Clear()
        {
            Window().Clear();
        }

        [McpTool("floatingorigin_move_window",
            "Moves the window of KSP Diag - Floating Origin, as dragging it does: x and y in pixels from " +
            "the top left corner of the screen. Returns its position and size (x, y, width, height).")]
        internal static object MoveWindow(double x, double y)
        {
            KSPDiagFloatingOrigin window = Window();
            Rect rect = window.WindowRect;
            rect.x = (float)x;
            rect.y = (float)y;
            window.WindowRect = rect;
            return new Dictionary<string, object>
            {
                { "x", (double)rect.x },
                { "y", (double)rect.y },
                { "width", (double)rect.width },
                { "height", (double)rect.height }
            };
        }

        // The window of this mod in the current scene; the window only exists in flight.
        private static KSPDiagFloatingOrigin Window()
        {
            KSPDiagFloatingOrigin window = UnityEngine.Object.FindObjectOfType<KSPDiagFloatingOrigin>();
            if (window == null)
            {
                throw new InvalidOperationException("The window of KSP Diag - Floating Origin only exists in flight");
            }
            return window;
        }
    }
}
