export const API_URL =
  process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000';

const TOKEN_KEY = 'state-sandbox-token';

class ApiClient {
  async _post(endpoint, data) {
    const res = await fetch(`${API_URL}${endpoint}`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        Authorization: `Bearer ${localStorage.getItem(TOKEN_KEY)}`,
      },
      body: JSON.stringify(data),
    });

    if (!res.ok) {
      const errorData = await res.json();
      throw new Error(errorData.detail || `API error: ${res.statusText}`);
    }

    return res.json();
  }

  async _postStream(endpoint, data, onMessage) {
    const res = await fetch(`${API_URL}${endpoint}`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        Authorization: `Bearer ${localStorage.getItem(TOKEN_KEY)}`,
      },
      body: JSON.stringify(data),
    });

    if (!res.ok) {
      const errorData = await res.json();
      throw new Error(errorData.detail || `API error: ${res.statusText}`);
    }

    const reader = res.body.getReader();
    const decoder = new TextDecoder();
    let buffer = '';

    while (true) {
      const { done, value } = await reader.read();
      if (done) break;

      buffer += decoder.decode(value, { stream: true });
      const lines = buffer.split('\n');
      buffer = lines.pop() || '';

      for (const line of lines) {
        if (line.trim()) {
          const event = JSON.parse(line);
          onMessage(event);
        }
      }
    }

    if (buffer.trim()) {
      const event = JSON.parse(buffer);
      onMessage(event);
    }
  }

  async _get(endpoint, params) {
    const url = new URL(`${API_URL}${endpoint}`);
    if (params) {
      Object.entries(params).forEach(([key, value]) => {
        if (value !== undefined && value !== null) {
          url.searchParams.append(key, value);
        }
      });
    }

    const res = await fetch(url, {
      headers: {
        Authorization: `Bearer ${localStorage.getItem(TOKEN_KEY)}`,
      },
    });

    if (!res.ok) {
      const errorData = await res.json();
      throw new Error(errorData.detail || `API error: ${res.statusText}`);
    }

    return res.json();
  }

  async _delete(endpoint) {
    const res = await fetch(`${API_URL}${endpoint}`, {
      method: 'DELETE',
      headers: {
        Authorization: `Bearer ${localStorage.getItem(TOKEN_KEY)}`,
      },
    });

    if (!res.ok) {
      const errorData = await res.json();
      throw new Error(errorData.detail || `API error: ${res.statusText}`);
    }

    return res.json();
  }

  async _patch(endpoint, data) {
    const res = await fetch(`${API_URL}${endpoint}`, {
      method: 'PATCH',
      headers: {
        'Content-Type': 'application/json',
        Authorization: `Bearer ${localStorage.getItem(TOKEN_KEY)}`,
      },
      body: JSON.stringify(data),
    });

    if (!res.ok) {
      const errorData = await res.json();
      throw new Error(errorData.detail || `API error: ${res.statusText}`);
    }

    return res.json();
  }

  async getLatestSnapshots(valueKeys) {
    return this._get('/api/states/latest', { valueKeys: valueKeys.join(',') });
  }

  async createAccount(username, email) {
    const data = await this._post('/api/auth/create', { username, email });
    localStorage.setItem(TOKEN_KEY, data.token);
    return data.user;
  }

  async getCurrentUser() {
    return this._get('/api/auth/me');
  }

  async getStates() {
    return this._get('/api/states');
  }

  async getStateSnapshots(stateId) {
    return this._get(`/api/states/${stateId}/snapshots`);
  }

  async createState(name, questions, onMessage) {
    return this._postStream('/api/states', { name, questions }, onMessage);
  }

  async getState(stateId) {
    return this._get(`/api/states/${stateId}`);
  }

  async createStateSnapshot(stateId, policy, onMessage) {
    return this._postStream(
      `/api/states/${stateId}/snapshots`,
      { policy },
      onMessage
    );
  }

  async getStateAdvice(stateId, question, events) {
    return this._post(`/api/states/${stateId}/advice`, {
      question,
      events: events?.join('\n') || '',
    });
  }

  async emailLogin(token) {
    const res = await this._get(`/api/auth/email-login/${token}`);
    localStorage.setItem(TOKEN_KEY, res.token);
    return res.user;
  }
}

// Export singleton instance
export const api = new ApiClient();
