document.getElementById('vibe-form').addEventListener('submit', async (e) => {
    e.preventDefault();
    
    const btn = document.getElementById('submit-btn');
    const originalText = btn.innerHTML;
    
    btn.innerHTML = `
        <svg class="animate-spin -ml-1 mr-3 h-5 w-5 text-white" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
            <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle>
            <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
        </svg>
        Agent Analyzing Frameworks...
    `;
    btn.classList.add('opacity-70', 'cursor-not-allowed');

    const formData = new FormData(e.target);

    try {
        // This will connect to your local laptop backend while you demo the live site
        const response = await fetch('http://127.0.0.1:8000/api/generate-roadmap', {
            method: 'POST',
            body: formData
        });
        
        if (!response.ok) throw new Error(`Backend not reached! Ensure your laptop server is running.`);
        
        const result = await response.json();

        if(result.status === 'success') {
            document.getElementById('input-section').classList.add('hidden');
            const dashboard = document.getElementById('dashboard');
            dashboard.classList.remove('hidden');
            buildDashboard(result);
        }
    } catch (error) {
        console.error('Error:', error);
        alert(error.message);
    } finally {
        btn.innerHTML = originalText;
        btn.classList.remove('opacity-70', 'cursor-not-allowed');
    }
});

function buildDashboard(result) {
    const dashboard = document.getElementById('dashboard');
    const data = result.data;
    
    let html = `
        <div class="bg-gray-900 rounded-2xl border border-gray-800 shadow-2xl overflow-hidden mb-8">
            <div class="p-8 border-b border-gray-800 flex flex-col md:flex-row justify-between items-start md:items-center bg-gray-800/50 gap-4">
                <div>
                    <h2 class="text-3xl font-bold mb-1">Your 30-Day Blueprint</h2>
                    <p class="text-gray-400">Target: <span class="text-white font-semibold">${result.role_analyzed}</span></p>
                </div>
                <div class="text-left md:text-right bg-gray-900 p-4 rounded-xl border border-gray-700 w-full md:w-auto">
                    <p class="text-sm text-gray-400 uppercase tracking-wider mb-1">Market Value Increase</p>
                    <p class="text-3xl font-extrabold text-green-400">+${data.market_value_increase}</p>
                </div>
            </div>
            
            <div class="p-8">
                <div class="mb-8 p-5 bg-gray-800/50 rounded-xl border border-gray-700">
                    <h3 class="text-lg font-semibold mb-2 text-neon">Agent Analysis:</h3>
                    <p class="text-sm text-gray-300 leading-relaxed">
                        Extracted <span class="text-neon font-bold">${data.user_skills_found.length}</span> skills. 
                        Target gaps: <span class="text-white">${data.missing_skills.join(', ')}</span>.
                    </p>
                </div>
                <div class="space-y-4">
    `;

    data.roadmap.forEach(item => {
        html += `
            <div class="bg-gray-800 p-5 rounded-xl flex justify-between items-center border border-gray-700 hover:border-neon transition group">
                <div class="flex items-center gap-4">
                    <div class="bg-gray-900 w-10 h-10 rounded-lg flex items-center justify-center font-bold text-neon border border-gray-700 group-hover:border-neon">
                        ${item.day}
                    </div>
                    <span class="font-medium text-gray-200">${item.task}</span>
                </div>
                <span class="text-xs font-bold text-gray-400 bg-gray-900 px-3 py-1 rounded-full">+${item.points} XP</span>
            </div>
        `;
    });

    html += `</div></div></div>`;
    dashboard.innerHTML = html;
}
