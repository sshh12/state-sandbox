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

  async _get(endpoint) {
    const res = await fetch(`${API_URL}${endpoint}`, {
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

  async _get_stream(endpoint, params = {}, onMessage) {
    if (typeof params === 'function' && !onMessage) {
      onMessage = params;
      params = {};
    }

    const searchParams = new URLSearchParams({
      ...params,
      token: localStorage.getItem(TOKEN_KEY),
    });

    const eventSource = new EventSource(
      `${API_URL}${endpoint}?${searchParams.toString()}`
    );

    return new Promise((resolve, reject) => {
      eventSource.onmessage = (event) => {
        onMessage?.(event.data);
      };

      eventSource.onerror = (error) => {
        eventSource.close();
        console.warning(error);
        resolve();
      };

      eventSource.addEventListener('complete', () => {
        eventSource.close();
        resolve();
      });
    });
  }

  async createAccount() {
    const data = await this._post('/api/auth/create', {});
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

  async createState(name, questions) {
    return this._post('/api/states', { name, questions });
  }

  async getState(stateId) {
    return this._get(`/api/states/${stateId}`);
  }

  async createStateSnapshot(stateId, policy) {
    return this._post(`/api/states/${stateId}/snapshots`, { policy });
  }

  async getStateAdvice(stateId, question) {
    return this._post(`/api/states/${stateId}/advice`, { question });
  }
}

// Export singleton instance
export const api = new ApiClient();
