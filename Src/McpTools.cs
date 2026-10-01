using System;
using System.Collections.Generic;
using UnityEngine;
using com.github.lhervier.ksp.mcpserver;

namespace com.github.lhervier.ksp.terrainprecisionfixdiag3
{
    /// <summary>
    /// What KSP-MCPServer, when it is installed, offers of this mod as tools: its buttons, the reading of
    /// its table, and the moving of its window. Each method works on the window loaded in the scene.
    /// Nothing here is needed to play by hand, and this mod runs the same without KSP-MCPServer: only
    /// that server reads the attribute.
    /// </summary>
    internal static class McpTools
    {
        [McpTool("diag3_record",
            "Presses Record in the window of Terrain Precision Fix Diag 3: freezes the line in progress into " +
                "its table and returns it (UniversalTime, RotatingFrame, DirectRotAngle, InverseRotAngle, " +
                "SphereOrigin, OriginDistance, Shifts since the line before, LastShift); null when there is no " +
                "body to read.")]
        internal static object Record()
        {
            return Window().Record();
        }

        [McpTool("diag3_read",
            "Reads the window of Terrain Precision Fix Diag 3: its recorded lines and the line in " +
                "progress.")]
        internal static object Read()
        {
            TerrainPrecisionFixDiag3Mod window = Window();
            return new Dictionary<string, object>
            {
                { "lines", new List<Reading>(window.Lines) },
                { "live", window.Live }
            };
        }

        [McpTool("diag3_clear", "Presses Clear table in the window of Terrain Precision Fix Diag 3.")]
        internal static void Clear()
        {
            Window().Clear();
        }

        [McpTool("diag3_move_window",
            "Moves the window of Terrain Precision Fix Diag 3, as dragging it does: x and y in pixels from " +
            "the top left corner of the screen. Returns its position and size (x, y, width, height).")]
        internal static object MoveWindow(double x, double y)
        {
            TerrainPrecisionFixDiag3Mod window = Window();
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
        private static TerrainPrecisionFixDiag3Mod Window()
        {
            TerrainPrecisionFixDiag3Mod window = UnityEngine.Object.FindObjectOfType<TerrainPrecisionFixDiag3Mod>();
            if (window == null)
            {
                throw new InvalidOperationException("The window of Terrain Precision Fix Diag 3 only exists in flight");
            }
            return window;
        }
    }
}
