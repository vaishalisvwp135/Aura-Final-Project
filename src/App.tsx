import React, { useState, FC } from 'react';
import './style.css';


export const App: FC<{ name: string }> = ({ name }) => {
  const [syllabus, setSyllabus] = useState('');

  return (
    <div style={{ padding: '20px', fontFamily: 'sans-serif', backgroundColor: '#f4f7f6', minHeight: '100vh' }}>
      <header style={{ borderBottom: '2px solid #007bff', marginBottom: '20px', paddingBottom: '10px' }}>
        <h1 style={{ color: '#007bff', margin: 0 }}>Aura: AI-Adaptive Study Architect</h1>
        <p style={{ color: '#555' }}>Step 1: System Initialization Complete</p>
      </header>

      <div style={{ display: 'flex', gap: '20px', flexDirection: 'row' }}>
        {/* Left Side: User Input */}
        <div style={{ flex: 1, backgroundColor: 'white', padding: '20px', borderRadius: '8px', boxShadow: '0 2px 5px rgba(0,0,0,0.1)' }}>
          <h3 style={{ marginTop: 0 }}>📋 Paste Your Syllabus</h3>
          <textarea 
            placeholder="Example: Unit 1 - Introduction to Java, Data Types, Loops..." 
            style={{ width: '100%', height: '150px', padding: '10px', boxSizing: 'border-box', borderRadius: '4px', border: '1px solid #ddd' }}
            value={syllabus}
            onChange={(e) => setSyllabus(e.target.value)}
          />
          <button style={{ width: '100%', marginTop: '10px', padding: '12px', backgroundColor: '#007bff', color: 'white', border: 'none', borderRadius: '4px', cursor: 'pointer', fontWeight: 'bold' }}>
            GENERATE ATOMIC TASKS
          </button>
          <div style={{marginTop:'30px',padding:'15px',backgroundColor:'#fff4e5', borderRadius: '4px', borderLeft: '5px solid #ffa500' }}>
           <h4 style={{ margin: '0 0 10px 0', color: '#cc8400' }}>🎯 Daily Focus Goal</h4>
           <p style={{ margin: 0, fontSize: '14px' }}>Target: 3 Atomic Tasks / Day</p>
           <p style={{ margin: '5px 0 0 0', fontSize: '12px', color: '#666' }}>Velocity Engine: Initializing...</p>
         </div>
        </div>

        {/* Right Side: AI Output Placeholder */}
        <div style={{ flex: 1, backgroundColor: '#ffffff', padding: '20px', borderRadius: '8px', border: '2px dashed #007bff' }}>
          <h3 style={{ marginTop: 0 }}>🤖 AI Task Breakdown</h3>
          <p style={{ color: '#888' }}>
            {syllabus.length > 0 ? "Ready to process..." : "Awaiting input text..."}
          </p>
          <div style={{ marginTop: '20px', height: '10px', backgroundColor: '#eee', borderRadius: '5px' }}>
            <div style={{ width: '30%', height: '100%', backgroundColor: '#007bff', borderRadius: '5px' }}></div>
          </div>
          <p style={{ fontSize: '12px', color: '#007bff' }}>Project Progress: 10% (Setup Done)</p>
        </div>
      </div>
    </div>
  );
};