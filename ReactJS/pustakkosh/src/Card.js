import React from 'react';
export default function Card (props) {
    const {donor} = props;
  return (
    <div className="col-md-4 mt-3">
         
        <div class="card cat-card" style={{ "width": "18rem" }}>
                        <div class="card-body m-3">
                            <h5 class="card-title">{donor.username}</h5>
                            <h6 class="card-subtitle mb-2 text-muted">&nbsp;</h6>
                            <p class="card-text">{donor.email}</p>
                        </div>
                    </div>
    </div>
  )
}